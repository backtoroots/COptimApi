import pytest

from framework.api import Api
from framework.contants import ApiConstants


@pytest.fixture(scope="session")
def api_client():
    yield Api(base_address=ApiConstants.URL_BASE)
