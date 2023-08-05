# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import os
from pathlib import Path

from azureml.featurestore._utils.utils import PathType, _parse_path_format
from azureml.featurestore.contracts.column import ColumnType
from azureml.featurestore.contracts.feature_source import SourceType
from marshmallow import fields, post_load, validates

from azure.ai.ml._schema import NestedField
from azure.ai.ml._schema._feature_set import FeatureSetSpecificationSchema, MaterializationSettingsSchema
from azure.ai.ml._schema.core.schema import PatchedSchemaMeta, YamlFileSchema
from azure.ai.ml.constants._common import BASE_PATH_CONTEXT_KEY
from azure.ai.ml.exceptions import ErrorCategory, ErrorTarget, ValidationErrorType, ValidationException


class DateTimeOffset(metaclass=PatchedSchemaMeta):
    days = fields.Integer(strict=True)
    hours = fields.Integer(strict=True)
    minutes = fields.Integer(strict=True)

    @post_load
    def make(self, data, **kwargs):
        from ..contracts.datetimeoffset import DateTimeOffset

        return DateTimeOffset(**data)


class TimestampColumnSchema(metaclass=PatchedSchemaMeta):
    name = fields.Str(required=True, allow_none=False)
    format = fields.Str(required=False, allow_none=True)

    @post_load
    def make(self, data, **kwargs):
        from ..contracts.timestamp_column import TimestampColumn

        return TimestampColumn(**data)


class Source(metaclass=PatchedSchemaMeta):
    type = fields.Str(required=True, allow_none=False)
    path = fields.Str(required=True, allow_none=False)
    timestamp_column = NestedField(TimestampColumnSchema, required=True, allow_none=False)
    source_delay = NestedField(DateTimeOffset)

    @post_load
    def make(self, data, **kwargs):
        from ..contracts.feature_source import FeatureSource

        data["type"] = SourceType[data["type"]]
        code_path_type, _ = _parse_path_format(data["path"])

        if code_path_type == PathType.local:
            source_path = Path(data["path"])
            if not source_path.is_absolute():
                source_path = Path(self.context.get(BASE_PATH_CONTEXT_KEY, os.getcwd()), source_path).resolve()
            data["path"] = source_path.as_posix()

        return FeatureSource(**data)


class ColumnSchema(metaclass=PatchedSchemaMeta):
    name = fields.Str(required=True, allow_none=False)
    type = fields.Str(required=True, allow_none=False)

    @post_load
    def make(self, data, **kwargs):
        from ..contracts.column import Column

        data["type"] = ColumnType[data["type"]]
        return Column(**data)


class Feature(metaclass=PatchedSchemaMeta):
    name = fields.Str(required=True, allow_none=False)
    type = fields.Str(required=True, allow_none=False)
    description = fields.Str()
    tags = fields.Dict(keys=fields.Str(), values=fields.Str())

    @post_load
    def make(self, data, **kwargs):
        from ..contracts.feature import Feature

        data["type"] = ColumnType[data["type"]]
        return Feature(**data)


class TransformationCode(metaclass=PatchedSchemaMeta):
    path = fields.Str(required=True, allow_none=False)
    transformer_class = fields.Str(required=True, allow_none=False)

    @post_load
    def make(self, data, **kwargs):
        from ..contracts.transformation_code import TransformationCode

        return TransformationCode(**data)


class FeatureSetSpecSchema(YamlFileSchema):
    source = NestedField(Source, required=True, allow_none=False)
    feature_transformation_code = NestedField(TransformationCode, required=False, allow_none=True)
    features = fields.List(NestedField(Feature), required=False, allow_none=True)
    index_columns = fields.List(NestedField(ColumnSchema), required=True, allow_none=False)
    source_lookback = NestedField(DateTimeOffset)
    temporal_join_lookback = NestedField(DateTimeOffset)

    @validates("source")
    def validate_specification_path(self, source):
        path_type, _ = _parse_path_format(source.path)
        if path_type == PathType.local:
            raise ValidationException(
                message="Feature source path: {} must be cloud path".format(source.path),
                no_personal_data_message="Feature source path must be cloud path",
                error_type=ValidationErrorType.INVALID_VALUE,
                error_category=ErrorCategory.USER_ERROR,
                target=ErrorTarget.GENERAL,
            )

    @post_load
    def make(self, data, **kwargs):
        from ..feature_set_spec import FeatureSetSpec

        return FeatureSetSpec(base_path=self.context[BASE_PATH_CONTEXT_KEY], **data)


class FeatureSetSchema(YamlFileSchema):
    name = fields.Str(required=True, allow_none=False)
    version = fields.Str(required=True, allow_none=False)
    specification = NestedField(FeatureSetSpecificationSchema, required=True, allow_none=False)
    entities = fields.List(fields.Str, required=True, allow_none=False)
    stage = fields.Str()
    description = fields.Str()
    tags = fields.Dict(keys=fields.Str(), values=fields.Str())
    materialization_settings = NestedField(MaterializationSettingsSchema)

    @validates("specification")
    def validate_specification_path(self, specification):
        pass

    @post_load
    def make(self, data, **kwargs):
        from .._feature_set import FeatureSet

        spec_path = Path(data["specification"].path)
        if not spec_path.is_absolute():
            spec_path = Path(self.context.get(BASE_PATH_CONTEXT_KEY, os.getcwd()), spec_path).resolve()
        data["specification"].path = spec_path.as_posix()
        return FeatureSet(base_path=self.context[BASE_PATH_CONTEXT_KEY], **data)
