# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------


def _get_lookup_key(featureset, row):
    suffix_parts = []

    for entity in featureset.entities:
        for index_column in entity.index_columns:
            suffix_parts.append(index_column.name)
            suffix_parts.append(row[index_column.name])

    prefix = f"featurestore:{featureset.feature_store_guid}:featureset:{featureset.name}:version:{featureset.version}"
    suffix = ":".join(suffix_parts)
    return f"{prefix}:{suffix}"
