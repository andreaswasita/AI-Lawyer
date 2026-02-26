"""
Unit tests for the authentication endpoints.
"""


def test_register_returns_tokens(client):
    payload = {
        "email": "test@example.com",
        "password": "securepassword123",
        "full_name": "Test User",
        "phone": "+6281234567890",
        "language": "id",
    }
    response = client.post("/api/v1/auth/register", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data
    assert data["token_type"] == "bearer"


def test_register_requires_minimum_password_length(client):
    payload = {
        "email": "short@example.com",
        "password": "short",  # < 8 characters
        "full_name": "Short Pass",
    }
    response = client.post("/api/v1/auth/register", json=payload)
    assert response.status_code == 422
    body = response.json()
    assert body["error"] is True
    assert "errors" in body


def test_register_requires_full_name(client):
    payload = {
        "email": "noname@example.com",
        "password": "securepassword123",
        "full_name": "A",  # < 2 characters
    }
    response = client.post("/api/v1/auth/register", json=payload)
    assert response.status_code == 422


def test_login_returns_tokens(client):
    payload = {"email": "user@example.com", "password": "anypassword"}
    response = client.post("/api/v1/auth/login", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data


def test_get_profile_returns_user(client):
    response = client.get("/api/v1/auth/me")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "email" in data
    assert "tier" in data


def test_logout_succeeds(client):
    response = client.post("/api/v1/auth/logout")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data


def test_refresh_token_returns_new_tokens(client):
    response = client.post(
        "/api/v1/auth/refresh", params={"refresh_token": "demo_refresh_token"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
