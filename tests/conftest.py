import copy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module

_ORIGINAL_ACTIVITIES = copy.deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset in-memory activities so tests do not leak state."""
    # Arrange
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(_ORIGINAL_ACTIVITIES))

    # Act
    yield

    # Assert
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(_ORIGINAL_ACTIVITIES))


@pytest.fixture
def client():
    # Arrange
    test_client = TestClient(app_module.app)

    # Act
    return test_client
