import pytest

@pytest.fixture
def headers():
    return {
        "Authorization": "Bearer ",
        "Content-Type": "application/json"
    }
