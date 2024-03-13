import os

import pytest
from dotenv import load_dotenv

from litres_diplome_tests import schemas


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()

base_url = 'https://api.litres.ru/foundation/api'
headers = {"Content-Type": "application/json"}
SCHEMA_INIT = os.path.abspath(schemas.__file__)
SCHEMA_DIR = os.path.dirname(SCHEMA_INIT)
