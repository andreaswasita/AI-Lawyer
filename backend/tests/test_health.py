"""
Unit tests for the health check endpoints.
"""


def test_root_returns_healthy(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "name" in data
    assert "version" in data


def test_health_endpoint_returns_healthy(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "services" in data


def test_api_health_check(client):
    response = client.get("/api/v1/health/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data


def test_api_readiness_check(client):
    response = client.get("/api/v1/health/ready")
    assert response.status_code == 200
    data = response.json()
    assert "ready" in data
    assert "checks" in data
    assert data["checks"]["api"] is True


def test_response_includes_request_id_header(client):
    """Every response should carry an X-Request-ID header (from the logging middleware)."""
    response = client.get("/")
    assert "x-request-id" in response.headers
