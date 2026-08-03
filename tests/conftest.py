import copy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture
def client():
    # Arrange
    original_activities = copy.deepcopy(app_module.activities)
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(original_activities))

    with TestClient(app_module.app) as test_client:
        # Act / Assert are handled in the individual tests
        yield test_client

    # Cleanup
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(original_activities))
