"""
Tests for the authentication endpoints.

Covers:
- User registration (success + duplicate email)
- Login (success + wrong password)
- Token refresh (success + invalid token)
- Profile retrieval (authenticated + unauthenticated)
- Logout
"""

import pytest


REGISTER_PAYLOAD = {
    "email": "test@example.com",
    "password": "securepass123",
    "full_name": "Test User",
    "phone": "+6281234567890",
    "language": "id",
}


# ── Registration ──────────────────────────────────────────────────────────


@pytest.mark.asyncio
async def test_register_success(client):
    response = await client.post("/api/v1/auth/register", json=REGISTER_PAYLOAD)
    assert response.status_code == 201
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data
    assert data["token_type"] == "bearer"
    assert data["expires_in"] == 1800


@pytest.mark.asyncio
async def test_register_duplicate_email(client):
    # First registration
    await client.post("/api/v1/auth/register", json=REGISTER_PAYLOAD)
    # Second registration with same email
    response = await client.post("/api/v1/auth/register", json=REGISTER_PAYLOAD)
    assert response.status_code == 409
    assert "already exists" in response.json()["detail"]


@pytest.mark.asyncio
async def test_register_password_too_short(client):
    payload = {**REGISTER_PAYLOAD, "email": "short@example.com", "password": "short"}
    response = await client.post("/api/v1/auth/register", json=payload)
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_register_missing_required_fields(client):
    response = await client.post("/api/v1/auth/register", json={"email": "x@x.com"})
    assert response.status_code == 422


# ── Login ─────────────────────────────────────────────────────────────────


@pytest.mark.asyncio
async def test_login_success(client):
    # Register first
    await client.post("/api/v1/auth/register", json=REGISTER_PAYLOAD)
    # Then login
    response = await client.post(
        "/api/v1/auth/login",
        json={"email": REGISTER_PAYLOAD["email"], "password": REGISTER_PAYLOAD["password"]},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


@pytest.mark.asyncio
async def test_login_wrong_password(client):
    await client.post("/api/v1/auth/register", json=REGISTER_PAYLOAD)
    response = await client.post(
        "/api/v1/auth/login",
        json={"email": REGISTER_PAYLOAD["email"], "password": "wrongpassword"},
    )
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_login_unknown_email(client):
    response = await client.post(
        "/api/v1/auth/login",
        json={"email": "nobody@example.com", "password": "anypassword"},
    )
    assert response.status_code == 401


# ── Token Refresh ─────────────────────────────────────────────────────────


@pytest.mark.asyncio
async def test_refresh_token_success(client):
    reg = await client.post("/api/v1/auth/register", json=REGISTER_PAYLOAD)
    refresh_token = reg.json()["refresh_token"]

    response = await client.post(
        "/api/v1/auth/refresh", json={"refresh_token": refresh_token}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data


@pytest.mark.asyncio
async def test_refresh_token_invalid(client):
    response = await client.post(
        "/api/v1/auth/refresh", json={"refresh_token": "this.is.not.valid"}
    )
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_refresh_token_using_access_token_fails(client):
    """Passing an access token as a refresh token should be rejected."""
    reg = await client.post("/api/v1/auth/register", json=REGISTER_PAYLOAD)
    access_token = reg.json()["access_token"]

    response = await client.post(
        "/api/v1/auth/refresh", json={"refresh_token": access_token}
    )
    assert response.status_code == 401


# ── Profile ───────────────────────────────────────────────────────────────


@pytest.mark.asyncio
async def test_get_profile_authenticated(client):
    reg = await client.post("/api/v1/auth/register", json=REGISTER_PAYLOAD)
    token = reg.json()["access_token"]

    response = await client.get(
        "/api/v1/auth/me", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == REGISTER_PAYLOAD["email"]
    assert data["full_name"] == REGISTER_PAYLOAD["full_name"]
    assert data["tier"] == "free"
    assert data["questions_limit"] == 5


@pytest.mark.asyncio
async def test_get_profile_unauthenticated(client):
    response = await client.get("/api/v1/auth/me")
    assert response.status_code in (401, 403)  # No Authorization header


@pytest.mark.asyncio
async def test_get_profile_invalid_token(client):
    response = await client.get(
        "/api/v1/auth/me", headers={"Authorization": "Bearer invalid.token.here"}
    )
    assert response.status_code == 401


# ── Logout ────────────────────────────────────────────────────────────────


@pytest.mark.asyncio
async def test_logout(client):
    response = await client.post("/api/v1/auth/logout")
    assert response.status_code == 200
    assert "logged out" in response.json()["message"].lower()
