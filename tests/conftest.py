import pytest
import database
from fastapi.testclient import TestClient
from main import app


@pytest.fixture(autouse=True, scope="session")
def clear_test_db():
    database.clear_db()

client = TestClient(app)