"""
Unit tests for the middleware (error handling and logging).
"""


def test_404_not_found_returns_structured_error(client):
    """Requesting a non-existent route should produce a 404 response."""
    response = client.get("/api/v1/this-does-not-exist")
    assert response.status_code == 404
    body = response.json()
    # The response contains either our structured error or FastAPI's default detail
    assert "error" in body or "detail" in body


def test_validation_error_returns_structured_error(client):
    """Sending an invalid payload should return a structured 422 with field errors."""
    # Empty message (min_length=1) should trigger validation error
    response = client.post("/api/v1/chat/", json={"message": "", "language": "id"})
    assert response.status_code == 422
    body = response.json()
    assert body["error"] is True
    assert "errors" in body
    assert len(body["errors"]) > 0


def test_request_id_header_present(client):
    """All responses must include an X-Request-ID header."""
    for path in ["/", "/health", "/api/v1/health/"]:
        response = client.get(path)
        assert "x-request-id" in response.headers, f"Missing X-Request-ID for {path}"


def test_missing_required_body_field_returns_422(client):
    """Omitting a required field should return 422."""
    response = client.post("/api/v1/auth/register", json={"email": "x@x.com"})
    assert response.status_code == 422
    body = response.json()
    assert body["error"] is True
