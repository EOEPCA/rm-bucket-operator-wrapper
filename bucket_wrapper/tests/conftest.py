from fastapi.testclient import TestClient
import pytest

from bucket_wrapper import app


@pytest.fixture
def client():
    return TestClient(app)
