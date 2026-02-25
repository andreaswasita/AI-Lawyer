"""
Pytest configuration and shared fixtures for the AI Lawyer backend tests.
"""

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(scope="session")
def client():
    """Return a synchronous TestClient for the FastAPI application."""
    with TestClient(app, raise_server_exceptions=False) as c:
        yield c
