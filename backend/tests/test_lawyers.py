"""
Unit tests for the lawyers (Advokat) endpoints.
"""


def test_list_lawyers_returns_list(client):
    response = client.get("/api/v1/lawyers/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_filter_lawyers_by_specialty(client):
    response = client.get("/api/v1/lawyers/?specialty=perceraian")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    for lawyer in data:
        assert "perceraian" in lawyer["specialties"]


def test_filter_lawyers_by_location(client):
    response = client.get("/api/v1/lawyers/?location=Jakarta")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    for lawyer in data:
        assert "jakarta" in lawyer["location"].lower()


def test_filter_lawyers_by_max_price(client):
    response = client.get("/api/v1/lawyers/?max_price=100000")
    assert response.status_code == 200
    data = response.json()
    for lawyer in data:
        assert lawyer["pricing"].get("chat", 0) <= 100000


def test_filter_lawyers_by_min_rating(client):
    response = client.get("/api/v1/lawyers/?min_rating=4.8")
    assert response.status_code == 200
    data = response.json()
    for lawyer in data:
        assert lawyer["rating"] >= 4.8


def test_get_specific_lawyer(client):
    response = client.get("/api/v1/lawyers/lawyer-001")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == "lawyer-001"
    assert "name" in data
    assert "specialties" in data


def test_get_nonexistent_lawyer_returns_404(client):
    response = client.get("/api/v1/lawyers/nonexistent-lawyer-xyz")
    assert response.status_code == 404
    body = response.json()
    assert body["error"] is True


def test_book_consultation_returns_booking(client):
    payload = {
        "lawyer_id": "lawyer-001",
        "consultation_type": "chat",
        "preferred_date": "2026-03-01",
        "preferred_time": "10:00",
        "topic": "Saya ingin konsultasi tentang perceraian",
        "language": "id",
    }
    response = client.post("/api/v1/lawyers/book", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "booking_id" in data
    assert data["lawyer_id"] == "lawyer-001"
    assert data["status"] == "pending_payment"


def test_book_consultation_with_unknown_lawyer_returns_404(client):
    payload = {
        "lawyer_id": "unknown-lawyer",
        "consultation_type": "chat",
        "preferred_date": "2026-03-01",
        "preferred_time": "10:00",
        "topic": "Test",
    }
    response = client.post("/api/v1/lawyers/book", json=payload)
    assert response.status_code == 404
    body = response.json()
    assert body["error"] is True
