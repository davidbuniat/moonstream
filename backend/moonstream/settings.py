import os

from bugout.app import Bugout

# Bugout
bugout_client = Bugout()

MOONSTREAM_APPLICATION_ID = os.environ.get("MOONSTREAM_APPLICATION_ID")
if MOONSTREAM_APPLICATION_ID is None:
    raise ValueError("MOONSTREAM_APPLICATION_ID environment variable must be set")

MOONSTREAM_DATA_JOURNAL_ID = os.environ.get("MOONSTREAM_DATA_JOURNAL_ID")
if MOONSTREAM_DATA_JOURNAL_ID is None:
    raise ValueError("MOONSTREAM_DATA_JOURNAL_ID environment variable must be set")

# Origin
RAW_ORIGINS = os.environ.get("MOONSTREAM_CORS_ALLOWED_ORIGINS")
if RAW_ORIGINS is None:
    raise ValueError(
        "MOONSTREAM_CORS_ALLOWED_ORIGINS environment variable must be set (comma-separated list of CORS allowed origins)"
    )
ORIGINS = RAW_ORIGINS.split(",")

# OpenAPI
DOCS_TARGET_PATH = "docs"
MOONSTREAM_OPENAPI_LIST = []
MOONSTREAM_OPENAPI_LIST_RAW = os.environ.get("MOONSTREAM_OPENAPI_LIST")
if MOONSTREAM_OPENAPI_LIST_RAW is not None:
    MOONSTREAM_OPENAPI_LIST = MOONSTREAM_OPENAPI_LIST_RAW.split(",")

DOCS_PATHS = {}
for path in MOONSTREAM_OPENAPI_LIST:
    DOCS_PATHS[f"/{path}/{DOCS_TARGET_PATH}"] = "GET"
    DOCS_PATHS[f"/{path}/{DOCS_TARGET_PATH}/openapi.json"] = "GET"
