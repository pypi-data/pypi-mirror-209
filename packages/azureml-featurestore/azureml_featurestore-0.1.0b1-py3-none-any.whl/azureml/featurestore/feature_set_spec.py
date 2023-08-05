# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import hashlib
import json
import os
from collections import OrderedDict
from datetime import datetime
from os import PathLike
from pathlib import Path
from typing import IO, TYPE_CHECKING, Dict, List, Optional, Union

import yaml
from azureml.featurestore._utils._constants import (
    FEATURE_SET_SPEC_YAML_FILENAME,
    FEATURE_SET_SPEC_YAML_FILENAME_FALLBACK,
    PACKAGE_NAME,
)
from azureml.featurestore._utils.utils import (
    PathType,
    _build_logger,
    _parse_path_format,
    _process_path,
    _strip_local_path,
)
from azureml.featurestore.contracts import Column, DateTimeOffset, FeatureSource, TransformationCode
from azureml.featurestore.contracts.feature import Feature
from azureml.featurestore.schema.feature_set_schema import FeatureSetSpecSchema
from marshmallow import EXCLUDE, ValidationError

from azure.ai.ml._exception_helper import log_and_raise_error
from azure.ai.ml._telemetry.activity import ActivityType, log_activity, monitor_with_activity
from azure.ai.ml._utils._experimental import experimental
from azure.ai.ml._utils.utils import dump_yaml_to_file
from azure.ai.ml.constants._common import BASE_PATH_CONTEXT_KEY
from azure.ai.ml.exceptions import ErrorCategory, ErrorTarget, MlException, ValidationErrorType, ValidationException
from azure.ai.ml.operations import DatastoreOperations

if TYPE_CHECKING:
    from pyspark.sql import DataFrame

package_logger = None


def _get_logger():
    global package_logger
    if package_logger is None:
        package_logger = _build_logger(__name__)
    return package_logger


@experimental
class FeatureSetSpec:
    """Represents a feature set specification.

    :param source: The underlying source data for this feature set
    :type source: FeatureSource
    :param features: Features in this feature set
    :type features: List[Feature]
    :param index_columns: Index columns for this feature set
    :type index_columns: List[DataColumn]
    :param feature_transformation_code: Transformation logic to be applied to the feature set
    :type feature_transformation_code: Code, optional
    :param source_lookback: A datetime representing window of source data fed to the feature transformation function.
                            This is needed for e.g. to calculate 30 day aggregate
    :type source_lookback: Datetime, optional
    :param temporal_join_lookback:  A datetime representing tolerance of the temporal join when the
                                    event data is joined with feature set
    :type temporal_join_lookback: Datetime, optional
    """

    def __init__(
        self,
        *,
        source: FeatureSource,
        index_columns: List[Column],
        features: List[Feature] = [],
        feature_transformation_code: Optional[TransformationCode] = None,
        source_lookback: Optional[DateTimeOffset] = None,
        temporal_join_lookback: Optional[DateTimeOffset] = None,
        base_path=None,
        **kwargs,
    ):
        """Initialize a feature set specification.

        :param source: The underlying source data for this feature set
        :type source: DataSource
        :param features: Features in this feature set
        :type features: List[Feature]
        :param index_columns: Index columns for this feature set
        :type index_columns: List[Column]
        :param feature_transformation_code: Transformation logic to be applied to the feature set
        :type feature_transformation_code: Code, optional
        :param source_lookback: A datetime representing window of source data fed to the feature transformation function.
                                This is needed for e.g. to calculate 30 day aggregate
        :type source_lookback: Datetime, optional
        :param temporal_join_lookback:  A datetime representing tolerance of the temporal join when the
                                        event data is joined with feature set
        :type temporal_join_lookback: Datetime, optional
        """

        with log_activity(_get_logger(), f"{PACKAGE_NAME}->FeatureSetSpec.Init", ActivityType.PUBLICAPI):
            self._base_path = base_path
            self.source = source
            self.features = features or []
            self.index_columns = index_columns or []
            self.feature_transformation_code = feature_transformation_code
            self.source_lookback = source_lookback
            self.temporal_join_lookback = temporal_join_lookback
            self._feature_transformation_code_local_path = None
            self._spec_folder_path = None

            # Generated name and version for offline join
            self.__name = hashlib.md5(self.__str__().encode()).hexdigest()
            self.__version = "1"

            if not self.source:
                msg = "Feature source is required for a feature set, please provide a feature source"
                raise ValidationException(
                    message=msg,
                    target=ErrorTarget.FEATURE_SET,
                    no_personal_data_message=msg,
                    error_category=ErrorCategory.USER_ERROR,
                    error_type=ValidationErrorType.MISSING_FIELD,
                )

            if len(self.index_columns) == 0:
                msg = "Index columns is required for a feature set, please provide non empty index columns"
                raise ValidationException(
                    message=msg,
                    target=ErrorTarget.FEATURE_SET,
                    no_personal_data_message=msg,
                    error_category=ErrorCategory.USER_ERROR,
                    error_type=ValidationErrorType.MISSING_FIELD,
                )

    def __repr__(self):
        info = OrderedDict()
        info["source"] = self.source.__repr__()
        info["features"] = [f.__repr__() for f in self.features]
        info["index_columns"] = [f.__repr__() for f in self.index_columns]
        info["feature_transformation_code"] = self.feature_transformation_code.__repr__()
        info["source_lookback"] = self.source_lookback.__repr__()
        info["temporal_join_lookback"] = self.temporal_join_lookback.__repr__()

        formatted_info = json.dumps(info, indent=2)
        return "FeatureSetSpec\n{}".format(formatted_info)

    def __str__(self):
        return self.__repr__()

    def get_feature(self, name: str):
        if not isinstance(name, str):
            msg = "Name must be the string name of a feature in this feature set spec. Found: {}"
            raise ValidationException(
                message=msg.format(type(name)),
                no_personal_data_message=msg,
                error_type=ValidationErrorType.INVALID_VALUE,
                error_category=ErrorCategory.USER_ERROR,
                target=ErrorTarget.GENERAL,
            )

        for feature in self.features:
            if feature.name == name:
                feature.feature_set_reference = self
                return feature

        msg = "Feature '{}' not found in this feature set spec."
        raise ValidationException(
            message=msg.format(name),
            no_personal_data_message=msg,
            error_type=ValidationErrorType.INVALID_VALUE,
            error_category=ErrorCategory.USER_ERROR,
            target=ErrorTarget.GENERAL,
        )

    @property
    def name(self):
        return self.__name

    @property
    def version(self):
        return self.__version

    def dump(self, dest: Union[str, PathLike], **kwargs) -> None:
        """Dump the feature set spec into a file in yaml format. Destination mush be a folder path, the spec file name is assumed as FeatureSetSpec.yaml, and an exception is raised if the file exists.
        If there is a transformation code specified, it will be copied to destination folder as a subfolder named 'code', and an exception is raised if code folder exists.
        :param dest: The folder path destination to receive this spec.
        :type dest: Union[PathLike, str]
        """
        path_type, _ = _parse_path_format(dest)
        if path_type != PathType.local:
            msg = "Destination {} must be local path"
            raise ValidationException(
                message=msg.format(dest),
                target=ErrorTarget.FEATURE_SET,
                no_personal_data_message="Destination must be a local folder path",
                error_category=ErrorCategory.USER_ERROR,
                error_type=ValidationErrorType.INVALID_VALUE,
            )
        if not os.path.isdir(dest):
            msg = "Destination {} must be an existing folder path"
            raise ValidationException(
                message=msg.format(dest),
                target=ErrorTarget.FEATURE_SET,
                no_personal_data_message="Destination must be an existing folder path",
                error_category=ErrorCategory.USER_ERROR,
                error_type=ValidationErrorType.INVALID_VALUE,
            )

        if self.feature_transformation_code:
            import shutil

            origin_code_path = self.feature_transformation_code.path
            code_path = self.feature_transformation_code.path
            if self._spec_folder_path:
                code_path = os.path.join(self._spec_folder_path, _strip_local_path(code_path))
            shutil.copytree(src=code_path, dst=os.path.join(dest, "code"))
            self.feature_transformation_code.path = "./code"
            yaml_serialized = self._to_dict()
            self.feature_transformation_code.path = origin_code_path
        else:
            yaml_serialized = self._to_dict()

        dest = os.path.join(dest, FEATURE_SET_SPEC_YAML_FILENAME)

        if os.path.isfile(dest):
            msg = "Spec file {} already exists"
            raise ValidationException(
                message=msg.format(dest),
                target=ErrorTarget.FEATURE_SET,
                no_personal_data_message="Spec file already exists",
                error_category=ErrorCategory.USER_ERROR,
                error_type=ValidationErrorType.INVALID_VALUE,
            )

        dump_yaml_to_file(dest, yaml_serialized, default_flow_style=False, **kwargs)

    def _to_dict(self) -> Dict:
        # pylint: disable=no-member
        return FeatureSetSpecSchema(unknown=EXCLUDE, context={BASE_PATH_CONTEXT_KEY: "./"}).dump(self)

    @staticmethod
    def _load(config, config_file):
        from marshmallow import ValidationError

        context = {
            BASE_PATH_CONTEXT_KEY: Path(config_file).parent,
        }

        try:
            from .schema.feature_set_schema import FeatureSetSpecSchema

            config = FeatureSetSpecSchema(context=context).load(config)
        except ValidationError as ex:
            raise ValueError(ex.messages) from ex

        return config

    @classmethod
    @monitor_with_activity(_get_logger(), f"{PACKAGE_NAME}->FeatureSetSpec.FromConfig", ActivityType.PUBLICAPI)
    def from_config(
        cls, spec_path: Union[str, PathLike], datastore_operations: DatastoreOperations = None
    ) -> "FeatureSetSpec":
        """Load a feature set spec from yaml config. Spec path must be a folder path, the spec file name is assumed as FeatureSetSpec.yaml
        :param spec_path: The path to fetch this spec.
        :type spec_path: Union[str, PathLike]
        """
        try:
            local_spec_path = _process_path(path=spec_path, is_folder=True, datastore_operations=datastore_operations)

            if not os.path.isdir(local_spec_path):
                msg = "Spec path {} must be an existing folder path"
                raise ValidationException(
                    message=msg.format(spec_path),
                    target=ErrorTarget.FEATURE_SET,
                    no_personal_data_message="Spec path must be an existing folder path",
                    error_category=ErrorCategory.USER_ERROR,
                    error_type=ValidationErrorType.INVALID_VALUE,
                )
            spec_folder_path = local_spec_path
            local_spec_path = os.path.join(local_spec_path, FEATURE_SET_SPEC_YAML_FILENAME)

            try:
                with open(local_spec_path) as f:
                    cfg = yaml.safe_load(f)
            except FileNotFoundError:
                # Fall back to previous naming format
                local_spec_path = os.path.join(local_spec_path, FEATURE_SET_SPEC_YAML_FILENAME_FALLBACK)
                with open(local_spec_path) as f:
                    cfg = yaml.safe_load(f)
            except yaml.YAMLError as ex:
                raise ValueError(str(ex)) from ex

            spec = FeatureSetSpec._load(cfg, local_spec_path)
            if spec.feature_transformation_code:
                spec._feature_transformation_code_local_path = spec.feature_transformation_code._patch_zip(
                    os.path.dirname(local_spec_path), datastore_operations
                )

            spec._spec_folder_path = spec_folder_path

            return spec
        except ValidationError as ve:
            raise ValueError(
                f"Feature set yaml config validation error: field_name: {ve.field_name}, errors: {ve.messages}"
            )
        except Exception as ex:
            package_logger.error(f"{PACKAGE_NAME}->FeatureSetSpec.FromConfig, {type(ex).__name__}: {ex}")
            log_and_raise_error(error=ex, debug=True)

    @monitor_with_activity(_get_logger(), f"{PACKAGE_NAME}->FeatureSetSpec.ToSparkDataframe", ActivityType.PUBLICAPI)
    def to_spark_dataframe(
        self,
        *,
        featureWindowStartDateTime: datetime = None,
        featureWindowEndDateTime: datetime = None,
        features: List[str] = None,
        dedup: bool = False,
        **kwargs,
    ):
        """Display a feature set in a spark dataframe format, after performing necessary transformation
        :param featureWindowStartDateTime: The start data time of feature window
        :type featureWindowStartDateTime: datetime
        :param featureWindowEndDateTime: The end data time of feature window
        :type featureWindowEndDateTime: datetime
        :param features: List of feature names to show
        :type features: List[str]
        :return: feature set dataframe
        :rtype: DataFrame
        """
        try:
            from azureml.featurestore._utils.spark_utils import (
                _deduplicate_dataframe,
                _filter_dataframe,
                _load_source_data,
                _transform_dataframe,
            )
            from pyspark.sql import SparkSession

            # check spark session
            try:
                spark = SparkSession.builder.getOrCreate()
            except Exception:
                raise Exception("Fail to get spark session, please check if spark environment is set up.")

            timestamp_column, timestamp_column_format = self.get_timestamp_column()
            df = _load_source_data(
                spark,
                source_type=self.source.type,
                source_path=self.source.path,
                timestamp_column=timestamp_column,
                timestamp_column_format=timestamp_column_format,
                source_lookback=self.source_lookback,
                feature_window_start_time=featureWindowStartDateTime,
                feature_window_end_time=featureWindowEndDateTime,
            )

            # transform
            if self.feature_transformation_code:
                if not self._feature_transformation_code_local_path:
                    self._feature_transformation_code_local_path = self.feature_transformation_code._patch_zip()

                df = _transform_dataframe(
                    spark=spark,
                    source_df=df,
                    transformer_code_path=self._feature_transformation_code_local_path,
                    transformer_class=self.feature_transformation_code.transformer_class,
                )

            if "schema_validation" not in kwargs or kwargs["schema_validation"] is not False:
                # data schema check
                self.__validate_schema(df)

                if not features or len(features) == 0:
                    features = list(map(lambda f: f.name, self.features))

                index_columns = list(map(lambda i: i.name, self.get_index_columns()))

                df = _filter_dataframe(
                    spark=spark,
                    df=df,
                    featureWindowStartDateTime=featureWindowStartDateTime,
                    featureWindowEndDateTime=featureWindowEndDateTime,
                    index_columns=index_columns,
                    timestamp_column=timestamp_column,
                    features=features,
                )

                if dedup:
                    distinct_df, has_dup = _deduplicate_dataframe(
                        df=df, join_keys=index_columns, timestamp_column=timestamp_column
                    )
                    if has_dup:
                        total_count = df.count()
                        print(
                            f"There are multiple rows sharing the same join keys and event timestamp, source data has {total_count} rows, dropped {total_count - distinct_df.count()} duplicated rows"
                        )
                    df = distinct_df

            return df
        except Exception as ex:
            if isinstance(ex, MlException):
                _get_logger().error(
                    f"{PACKAGE_NAME}->FeatureSetSpec.ToSparkDataframe, {type(ex).__name__}: {ex.no_personal_data_message}"
                )
            else:
                _get_logger().error(f"{PACKAGE_NAME}->FeatureSetSpec.ToSparkDataframe, {type(ex).__name__}: {ex}")

            log_and_raise_error(error=ex, debug=True)

    def get_index_columns(self):
        return self.index_columns

    def get_timestamp_column(self):
        if not self.source.timestamp_column:
            # TODO: Suppport Non-timeseries data [prp2]
            msg = "Expected timestamp columns not found in feature set {}."
            raise ValidationException(
                message=msg.format(self.name),
                no_personal_data_message=msg,
                error_type=ValidationErrorType.MISSING_FIELD,
                error_category=ErrorCategory.USER_ERROR,
                target=ErrorTarget.GENERAL,
            )

        return self.source.timestamp_column.name, self.source.timestamp_column.format

    def __validate_schema(self, df: "DataFrame"):
        from azureml.featurestore._utils.type_map import TypeMap

        columns_set = set(df.columns)
        for feature in self.features:
            if feature.name not in columns_set:
                raise Exception("Schema check errors, no feature column: {} in output dataframe".format(feature.name))
            data_type = TypeMap.spark_to_column_type(df.schema[feature.name].dataType.typeName())
            expected_data_type = feature.type
            if data_type != expected_data_type:
                raise ValidationException(
                    message="Schema check errors, feature column: {} has data type: {}, expected: {}".format(
                        feature.name, data_type, expected_data_type
                    ),
                    no_personal_data_message="Schema check errors, feature column data type mismatch.",
                    error_type=ValidationErrorType.INVALID_VALUE,
                    error_category=ErrorCategory.USER_ERROR,
                    target=ErrorTarget.GENERAL,
                )

        for index_column in self.index_columns:
            if index_column.name not in columns_set:
                raise Exception(
                    "Schema check errors, no index column: {} in output dataframe".format(index_column.name)
                )
            data_type = TypeMap.spark_to_column_type(df.schema[index_column.name].dataType.typeName())
            expected_data_type = index_column.type
            if data_type != expected_data_type:
                raise ValidationException(
                    message="Schema check errors, index column: {} has data type: {}, expected: {}".format(
                        index_column.name, data_type, expected_data_type
                    ),
                    no_personal_data_message="Schema check errors, index column data type mismatch.",
                    error_type=ValidationErrorType.INVALID_VALUE,
                    error_category=ErrorCategory.USER_ERROR,
                    target=ErrorTarget.GENERAL,
                )


@monitor_with_activity(_get_logger(), f"{PACKAGE_NAME}->CreateFeatureSetSpec", ActivityType.PUBLICAPI)
def create_feature_set_spec(
    *,
    infer_schema: Optional[bool] = False,
    spec_path: Optional[Union[str, PathLike, IO[str]]] = None,
    source: Optional[FeatureSource] = None,
    features: Optional[List[Feature]] = [],
    index_columns: Optional[List[Column]] = [],
    transformation_code: Optional[TransformationCode] = None,
    source_lookback: Optional[DateTimeOffset] = None,
    temporal_join_lookback: Optional[DateTimeOffset] = None,
) -> FeatureSetSpec:
    """Utility for creating a FeatureSetSpec. If infer schema is True, infer the type for every column that is not an index column or timestamp column. Add all these columns and their column type to the Feature list of the returned FeatureSetSpec.
    :param infer_schema: whether to infer the schema
    :type infer_schema: bool, default: False
    :param spec_path: feature set spec path to infer from, required if other objects are not provided, will override other objects if provided.
    :type spec_path: Union[str, PathLike, IO[str]], optional
    :param source: FeatureSource object to be included in feature set spec result
    :type FeatureSource, optional
    :param features: List of Feature object to be included in feature set spec result
    :type features: List[Feature], optional
    :param index_columns: List of Index Column object to be included in feature set spec result
    :type index_columns: List[Column], optional
    :param transformation_code: Transformation code to be included in feature set spec result
    :type transformation_code: TransformationCode, optional
    :param source_lookback: source lookback to be included in feature set spec result
    :type source_lookback: DateTimeOffset, optional
    :param temporal_join_lookback: temporal join lookback to be included in feature set spec result
    :type temporal_join_lookback: DateTimeOffset, optional
    :return: Featureset Spec
    :rtype: FeaturesetSpec
    """
    try:
        if spec_path:
            feature_set_spec = FeatureSetSpec.from_config(spec_path=spec_path)
        else:
            feature_set_spec = FeatureSetSpec(
                source=source,
                features=features,
                index_columns=index_columns,
                feature_transformation_code=transformation_code,
                source_lookback=source_lookback,
                temporal_join_lookback=temporal_join_lookback,
            )

        if infer_schema:
            from azureml.featurestore._utils.type_map import TypeMap

            timestamp_column, _ = feature_set_spec.get_timestamp_column()
            df = feature_set_spec.to_spark_dataframe(
                featureWindowStartDateTime=None,
                featureWindowEndDateTime=None,
                features=None,
                dedup=False,
                schema_validation=False,
            )

            features = []
            index_columns_set = set([index_column.name for index_column in feature_set_spec.index_columns])

            for column_name in df.columns:
                if column_name != timestamp_column and column_name not in index_columns_set:
                    data_type = TypeMap.spark_to_column_type(df.schema[column_name].dataType.typeName())
                    features.append(Feature(name=column_name, type=data_type))
            feature_set_spec.features = features

            if len(feature_set_spec.features) == 0:
                msg = "Inferred feature set spec has empty features, please check feature source data."
                raise ValidationException(
                    message=msg,
                    target=ErrorTarget.FEATURE_SET,
                    no_personal_data_message=msg,
                    error_category=ErrorCategory.USER_ERROR,
                    error_type=ValidationErrorType.INVALID_VALUE,
                )

        return feature_set_spec
    except Exception as ex:
        if isinstance(ex, MlException):
            _get_logger().error(
                f"{PACKAGE_NAME}->CreateFeatureSetSpec, {type(ex).__name__}: {ex.no_personal_data_message}"
            )
        else:
            _get_logger().error(f"{PACKAGE_NAME}->CreateFeatureSetSpec, {type(ex).__name__}: {ex}")

        log_and_raise_error(error=ex, debug=True)
