import pytest


@pytest.fixture(scope="session")
def config_dict():
    return {
        "data": ...,
        "id": ...,
    }
