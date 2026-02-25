"""
Tests for the AI chat endpoint.

Covers:
- Sending a legal question (success)
- Input validation (empty message, too long)
- Category detection (triage)
- Query logging (entry written to DB)
- Legal categories listing
"""

import pytest
from sqlalchemy import select

from app.models.query_log import QueryLog


CHAT_URL = "/api/v1/chat/"


# ── Basic chat ────────────────────────────────────────────────────────────


@pytest.mark.asyncio
async def test_chat_basic_response(client):
    payload = {"message": "Bagaimana cara mengurus perceraian di Indonesia?", "language": "id"}
    response = await client.post(CHAT_URL, json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "conversation_id" in data
    assert "message" in data
    assert "triage" in data
    assert "disclaimer" in data


@pytest.mark.asyncio
async def test_chat_returns_conversation_id(client):
    """A new conversation ID should be generated when none is provided."""
    payload = {"message": "Apa itu PKWT?", "language": "id"}
    response = await client.post(CHAT_URL, json=payload)
    assert response.status_code == 200
    assert len(response.json()["conversation_id"]) == 36  # UUID


@pytest.mark.asyncio
async def test_chat_preserves_conversation_id(client):
    """An existing conversation ID should be echoed back."""
    conv_id = "test-conversation-id-1234"
    payload = {"message": "Pertanyaan lanjutan?", "conversation_id": conv_id, "language": "id"}
    response = await client.post(CHAT_URL, json=payload)
    assert response.status_code == 200
    assert response.json()["conversation_id"] == conv_id


@pytest.mark.asyncio
async def test_chat_english_language(client):
    payload = {"message": "How do I file for divorce in Indonesia?", "language": "en"}
    response = await client.post(CHAT_URL, json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "This is general information" in data["disclaimer"]


# ── Input validation ──────────────────────────────────────────────────────


@pytest.mark.asyncio
async def test_chat_empty_message_rejected(client):
    payload = {"message": "", "language": "id"}
    response = await client.post(CHAT_URL, json=payload)
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_chat_message_too_long_rejected(client):
    payload = {"message": "x" * 4001, "language": "id"}
    response = await client.post(CHAT_URL, json=payload)
    assert response.status_code == 422


# ── Triage ────────────────────────────────────────────────────────────────


@pytest.mark.asyncio
async def test_chat_triage_category_perceraian(client):
    payload = {"message": "Saya ingin cerai dari suami saya", "language": "id"}
    response = await client.post(CHAT_URL, json=payload)
    assert response.status_code == 200
    assert response.json()["triage"]["category"] == "perceraian"


@pytest.mark.asyncio
async def test_chat_triage_category_bisnis(client):
    payload = {"message": "Cara mendirikan PT di Indonesia", "language": "id"}
    response = await client.post(CHAT_URL, json=payload)
    assert response.status_code == 200
    assert response.json()["triage"]["category"] == "bisnis"


@pytest.mark.asyncio
async def test_chat_triage_has_confidence(client):
    payload = {"message": "Pertanyaan umum hukum", "language": "id"}
    response = await client.post(CHAT_URL, json=payload)
    triage = response.json()["triage"]
    assert 0.0 <= triage["confidence"] <= 1.0


# ── Query logging ─────────────────────────────────────────────────────────


@pytest.mark.asyncio
async def test_chat_query_logged_to_db(client, db_session):
    """Each chat message should create a QueryLog entry."""
    message = "Pertanyaan uji query log"
    payload = {"message": message, "language": "id"}
    response = await client.post(CHAT_URL, json=payload)
    assert response.status_code == 200

    conv_id = response.json()["conversation_id"]
    result = await db_session.execute(
        select(QueryLog).where(QueryLog.conversation_id == conv_id)
    )
    log = result.scalar_one_or_none()
    assert log is not None
    assert log.message == message
    assert log.language == "id"
    assert log.category is not None
    assert log.response_preview is not None


# ── Categories ────────────────────────────────────────────────────────────


@pytest.mark.asyncio
async def test_get_categories(client):
    response = await client.get(CHAT_URL + "categories")
    assert response.status_code == 200
    data = response.json()
    assert "categories" in data
    assert "perceraian" in data["categories"]
    assert "bisnis" in data["categories"]
