"""
Unit tests for the templates endpoints.
"""


def test_list_templates_returns_list(client):
    response = client.get("/api/v1/templates/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_filter_templates_by_category(client):
    response = client.get("/api/v1/templates/?category=perceraian")
    assert response.status_code == 200
    data = response.json()
    assert all(t["category"] == "perceraian" for t in data)


def test_filter_templates_by_free_tier(client):
    response = client.get("/api/v1/templates/?tier=free")
    assert response.status_code == 200
    data = response.json()
    assert all(t["tier"] == "free" for t in data)


def test_filter_templates_popular_only(client):
    response = client.get("/api/v1/templates/?popular=true")
    assert response.status_code == 200
    data = response.json()
    assert all(t["popular"] is True for t in data)


def test_search_templates(client):
    response = client.get("/api/v1/templates/?search=cerai")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0


def test_get_popular_templates(client):
    response = client.get("/api/v1/templates/popular")
    assert response.status_code == 200
    data = response.json()
    assert "templates" in data


def test_get_template_categories(client):
    response = client.get("/api/v1/templates/categories")
    assert response.status_code == 200
    data = response.json()
    assert "categories" in data


def test_get_specific_template(client):
    response = client.get("/api/v1/templates/surat-gugatan-cerai")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == "surat-gugatan-cerai"
    assert "fields" in data


def test_get_nonexistent_template_returns_404(client):
    response = client.get("/api/v1/templates/nonexistent-template-xyz")
    assert response.status_code == 404
    body = response.json()
    assert body["error"] is True
