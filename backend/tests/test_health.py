"""
Tests for the health check endpoints.
"""

import pytest


@pytest.mark.asyncio
async def test_root_health(client):
    response = await client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "name" in data
    assert "version" in data


@pytest.mark.asyncio
async def test_api_health(client):
    response = await client.get("/api/v1/health/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data


@pytest.mark.asyncio
async def test_readiness(client):
    response = await client.get("/api/v1/health/ready")
    assert response.status_code == 200
    data = response.json()
    assert "ready" in data
    assert "checks" in data
    assert data["checks"]["api"] is True
