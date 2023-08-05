# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

__path__ = __import__("pkgutil").extend_path(__path__, __name__)  # type: ignore

from .aml_hobospark_on_behalf_of import AzureMLHoboSparkOnBehalfOfCredential

__all__ = [
    "AzureMLHoboSparkOnBehalfOfCredential",
]
