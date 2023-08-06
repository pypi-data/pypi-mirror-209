from typing import Dict, List

from pyspark.sql import DataFrame

from databricks.feature_store.entities.feature_spec import FeatureSpec
from databricks.feature_store.entities.feature_table import FeatureTable
from databricks.feature_store.information_schema_spark_client import FunctionInfo
from databricks.feature_store.utils.feature_lookup_utils import (
    join_feature_data_if_not_overridden,
)
from databricks.feature_store.utils.on_demand_utils import (
    apply_functions_if_not_overridden,
)


class TrainingSet:
    """
    Class that defines :obj:`TrainingSet` objects.

    .. note::

       The :class:`TrainingSet` constructor should not be called directly. Instead,
       call :meth:`FeatureStoreClient.create_training_set <databricks.feature_store.client.FeatureStoreClient.create_training_set>`.
    """

    def __init__(
        self,
        feature_spec: FeatureSpec,
        df: DataFrame,
        labels: List[str],
        feature_table_metadata_map: Dict[str, FeatureTable],
        feature_table_data_map: Dict[str, DataFrame],
        uc_function_infos: Dict[str, FunctionInfo],
    ):
        """Initialize a :obj:`TrainingSet` object."""
        assert isinstance(
            labels, list
        ), f"Expected type `list` for argument `labels`. Got '{labels}' with type '{type(labels)}'."

        self._feature_spec = feature_spec
        self._df = df
        self._labels = labels
        self._feature_table_metadata_map = feature_table_metadata_map
        self._feature_table_data_map = feature_table_data_map
        self._uc_function_infos = uc_function_infos

    @property
    def feature_spec(self) -> FeatureSpec:
        """Define a feature spec."""
        return self._feature_spec

    def _augment_df(self) -> DataFrame:
        """
        Internal helper to augment DataFrame with feature lookups and on-demand features specified in the FeatureSpec.
        Does not drop excluded columns, and does not overwrite columns that already exist.
        Return column order is df.columns + feature lookups + on-demand features.
        """
        # Apply FeatureLookups
        df_with_features = join_feature_data_if_not_overridden(
            feature_spec=self.feature_spec,
            df=self._df,
            feature_table_metadata_map=self._feature_table_metadata_map,
            feature_table_data_map=self._feature_table_data_map,
        )
        # Apply all on-demand UDFs
        df_with_features_and_on_demand = apply_functions_if_not_overridden(
            feature_spec=self.feature_spec,
            df=df_with_features,
            uc_function_infos=self._uc_function_infos,
        )
        return df_with_features_and_on_demand

    def load_df(self) -> DataFrame:
        """
        Load a :class:`DataFrame <pyspark.sql.DataFrame>`.

        Return a :class:`DataFrame <pyspark.sql.DataFrame>` for training.

        The returned :class:`DataFrame <pyspark.sql.DataFrame>` has columns specified
        in the ``feature_spec`` and ``labels`` parameters provided
        in :meth:`FeatureStoreClient.create_training_set <databricks.feature_store.client.FeatureStoreClient.create_training_set>`.

        :return:
           A :class:`DataFrame <pyspark.sql.DataFrame>` for training
        """
        augmented_df = self._augment_df()
        # Return only included columns in order defined by FeatureSpec + labels
        included_columns = [
            ci.output_name for ci in self.feature_spec.column_infos if ci.include
        ] + self._labels
        return augmented_df.select(included_columns)
