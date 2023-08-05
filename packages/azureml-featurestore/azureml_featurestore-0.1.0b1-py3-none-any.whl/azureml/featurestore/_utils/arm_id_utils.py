# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import re

from azure.ai.ml.exceptions import ErrorCategory, ErrorTarget, ValidationErrorType, ValidationException


class FeatureStoreArmId(object):
    """Parser for FeatureStore arm id: e.g. /subscription/.../featurestore/...

    :param arm_id: The versioned ARM id.
    :type arm_id: str
    :raises ~azure.ai.ml.exceptions.ValidationException: Raised if the ARM id is incorrectly formatted.
    """

    REGEX_PATTERN = (
        r"^azureml://subscriptions/([a-zA-Z0-9_\-]+)/resourcegroups/([a-zA-Z0-9_\-]+)/workspaces/([a-zA-Z0-9_\-]+)$"
    )

    def __init__(self, arm_id=None):
        self.is_registry_id = None
        if arm_id:
            match = re.match(FeatureStoreArmId.REGEX_PATTERN, arm_id)
            if match:
                self.subscription_id = match.group(1)
                self.resource_group_name = match.group(2)
                self.workspace_name = match.group(3)
            else:
                msg = "Invalid AzureML ARM versioned Id {}"
                raise ValidationException(
                    message=msg.format(arm_id),
                    no_personal_data_message=msg.format("[arm_id]"),
                    error_type=ValidationErrorType.INVALID_VALUE,
                    error_category=ErrorCategory.USER_ERROR,
                    target=ErrorTarget.ARM_RESOURCE,
                )

    @staticmethod
    def to_uri(subscription_id, resource_group_name, workspace_name):
        return f"azureml://subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/workspaces/{workspace_name}"


class FeatureSetVersionedArmId(object):
    """Parser for FeatureSet versioned arm id: e.g. /subscription/.../featurestore/.../featureset/my-
    featureset/versions/1.

    :param arm_id: The versioned feature set ARM id.
    :type arm_id: str
    :raises ~azure.ai.ml.exceptions.ValidationException: Raised if the ARM id is incorrectly formatted.
    """

    REGEX_PATTERN = "^/?subscriptions/([^/]+)/resourceGroups/([^/]+)/providers/Microsoft.MachineLearningServices/workspaces/([^/]+)/featuresets/([^/]+)/versions/([^/]+)"

    def __init__(self, arm_id=None):
        self.is_registry_id = None
        if arm_id:
            match = re.match(FeatureSetVersionedArmId.REGEX_PATTERN, arm_id)
            if match:
                self.subscription_id = match.group(1)
                self.resource_group_name = match.group(2)
                self.workspace_name = match.group(3)
                self.featureset_name = match.group(4)
                self.featureset_version = match.group(5)
            else:
                msg = "Invalid AzureML ARM versioned Id {}"
                raise ValidationException(
                    message=msg.format(arm_id),
                    no_personal_data_message=msg.format("[arm_id]"),
                    error_type=ValidationErrorType.INVALID_VALUE,
                    error_category=ErrorCategory.USER_ERROR,
                    target=ErrorTarget.ARM_RESOURCE,
                )

    def __str__(self) -> str:
        return "/subscriptions/{}/resourceGroups/{}/providers/Microsoft.MachineLearningServices/workspaces/{}/featuresets/{}/versions/{}".format(
            self.subscription_id,
            self.resource_group_name,
            self.workspace_name,
            self.featureset_name,
            self.featureset_version,
        )

    def __repr__(self) -> str:
        return self.__str__()


class FeatureStoreEntityVersionedArmId(object):
    """Parser for FeatureStoreEntity versioned arm id: e.g. /subscriptions/.../.../featureentities/my-
    featureentity/versions/1.

    :param arm_id: The versioned feature entity ARM id.
    :type arm_id: str
    :raises ~azure.ai.ml.exceptions.ValidationException: Raised if the ARM id is incorrectly formatted.
    """

    REGEX_PATTERN = "^/?subscriptions/([^/]+)/resourceGroups/([^/]+)/providers/Microsoft.MachineLearningServices/workspaces/([^/]+)/featurestoreentities/([^/]+)/versions/([^/]+)"

    def __init__(self, arm_id):
        match = re.match(FeatureStoreEntityVersionedArmId.REGEX_PATTERN, arm_id)
        if match:
            self.subscription_id = match.group(1)
            self.resource_group_name = match.group(2)
            self.workspace_name = match.group(3)
            self.feature_store_entity_name = match.group(4)
            self.feature_store_entity_version = match.group(5)
        else:
            msg = "Invalid AzureML Feature Entity ARM versioned Id {}"
            raise ValidationException(
                message=msg.format(arm_id),
                no_personal_data_message=msg.format("[arm_id]"),
                error_type=ValidationErrorType.INVALID_VALUE,
                error_category=ErrorCategory.USER_ERROR,
                target=ErrorTarget.ARM_RESOURCE,
            )

    def __str__(self) -> str:
        return "/subscriptions/{}/resourceGroups/{}/providers/Microsoft.MachineLearningServices/workspaces/{}/featurestoreentities/{}/versions/{}".format(
            self.subscription_id,
            self.resource_group_name,
            self.workspace_name,
            self.feature_store_entity_name,
            self.feature_store_entity_version,
        )

    def __repr__(self) -> str:
        return self.__str__()


class OfflineStoreTargetArmId(object):
    """Parser for offline store arm id: e.g. /subscriptions/.../storageAccounts/.../containers/my-offlinesore-container

    :param arm_id: The offline store target ARM id.
    :type arm_id: str
    :raises ~azure.ai.ml.exceptions.ValidationException: Raised if the ARM id is incorrectly formatted.
    """

    REGEX_PATTERN = "^/?subscriptions/([^/]+)/resourceGroups/([^/]+)/providers/Microsoft.Storage/storageAccounts/([^/]+)/blobServices/default/containers/([^/]+)"

    def __init__(self, arm_id):
        match = re.match(OfflineStoreTargetArmId.REGEX_PATTERN, arm_id)
        if match:
            self.subscription_id = match.group(1)
            self.resource_group_name = match.group(2)
            self.storage_account = match.group(3)
            self.container_name = match.group(4)
        else:
            msg = "Invalid AzureML offlinestore target ARM Id {}"
            raise ValidationException(
                message=msg.format(arm_id),
                no_personal_data_message=msg.format("[arm_id]"),
                error_type=ValidationErrorType.INVALID_VALUE,
                error_category=ErrorCategory.USER_ERROR,
                target=ErrorTarget.ARM_RESOURCE,
            )

    def __str__(self) -> str:
        return "/subscriptions/{}/resourceGroups/{}/providers/Microsoft.Storage/storageAccounts/{}/blobServices/default/containers/{}".format(
            self.subscription_id,
            self.resource_group_name,
            self.storage_account,
            self.container_name,
        )

    def __repr__(self) -> str:
        return self.__str__()

    def to_abfs_path(self) -> str:
        return "abfs://{}@{}.dfs.core.windows.net".format(self.container_name, self.storage_account)
