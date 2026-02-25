"""
Unit tests for the AI chat endpoints.
"""


def test_send_message_returns_response(client):
    payload = {
        "message": "Bagaimana cara mengurus perceraian di Indonesia?",
        "language": "id",
    }
    response = client.post("/api/v1/chat/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "conversation_id" in data
    assert "message" in data
    assert "triage" in data
    assert "disclaimer" in data


def test_send_message_english(client):
    payload = {
        "message": "How do I register a company in Indonesia?",
        "language": "en",
    }
    response = client.post("/api/v1/chat/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["triage"]["category"] == "bisnis"


def test_send_message_preserves_conversation_id(client):
    conv_id = "test-conversation-123"
    payload = {"message": "Apa hak karyawan?", "conversation_id": conv_id}
    response = client.post("/api/v1/chat/", json=payload)
    assert response.status_code == 200
    assert response.json()["conversation_id"] == conv_id


def test_send_message_requires_non_empty_message(client):
    payload = {"message": "", "language": "id"}
    response = client.post("/api/v1/chat/", json=payload)
    assert response.status_code == 422
    body = response.json()
    assert body["error"] is True


def test_send_message_too_long_is_rejected(client):
    payload = {"message": "x" * 4001, "language": "id"}
    response = client.post("/api/v1/chat/", json=payload)
    assert response.status_code == 422


def test_get_categories_returns_dict(client):
    response = client.get("/api/v1/chat/categories")
    assert response.status_code == 200
    data = response.json()
    assert "categories" in data
    assert "perceraian" in data["categories"]


def test_triage_detects_divorce_category(client):
    payload = {"message": "saya ingin cerai dari suami saya", "language": "id"}
    response = client.post("/api/v1/chat/", json=payload)
    assert response.status_code == 200
    assert response.json()["triage"]["category"] == "perceraian"


def test_triage_detects_employment_category(client):
    payload = {"message": "saya kena PHK tanpa pesangon", "language": "id"}
    response = client.post("/api/v1/chat/", json=payload)
    assert response.status_code == 200
    assert response.json()["triage"]["category"] == "ketenagakerjaan"


def test_complex_case_recommends_lawyer(client):
    payload = {"message": "saya ingin mengajukan gugatan ke pengadilan", "language": "id"}
    response = client.post("/api/v1/chat/", json=payload)
    assert response.status_code == 200
    assert response.json()["triage"]["recommendation"] == "lawyer_consultation"
