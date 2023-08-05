# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from typing import List

import pyarrow
import pyarrow.flight as flight
from azureml.featurestore.contracts.feature import Feature


class FlightFeatureRetrievalClient:
    def __init__(self, uri):
        self.location = flight.Location(uri)
        self.connection = flight.connect(self.location)
        self.connection.wait_for_available()

    def get_online_features(self, features: List[Feature], observation_df: "pandas.DataFrame"):
        descriptor = flight.FlightDescriptor.for_path("online", *[f.uri for f in features])
        writer, reader = self.connection.do_exchange(descriptor)

        writer.begin(pyarrow.Schema.from_pandas(observation_df))
        writer.write_table(pyarrow.Table.from_pandas(observation_df))
        writer.done_writing()

        features_df = reader.read_pandas()
        writer.close()

        return features_df

    def get_offline_features(
        self, features: List[Feature], observation_df: "pyspark.sql.DataFrame", timestamp_column: str
    ):
        descriptor = flight.FlightDescriptor.for_path(f"offline:{timestamp_column}", *[f.uri for f in features])
        raise NotImplementedError()
