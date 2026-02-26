"""
Unit tests for the legal database endpoints.
"""


def test_list_all_references(client):
    response = client.get("/api/v1/legal-db/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    # Check structure of first item
    item = data[0]
    assert "id" in item
    assert "law_name" in item
    assert "category" in item


def test_filter_by_category(client):
    response = client.get("/api/v1/legal-db/?category=bisnis")
    assert response.status_code == 200
    data = response.json()
    assert all(item["category"] == "bisnis" for item in data)


def test_filter_by_unknown_category_returns_404(client):
    response = client.get("/api/v1/legal-db/?category=unknown_category_xyz")
    assert response.status_code == 404
    body = response.json()
    assert body["error"] is True


def test_search_returns_relevant_results(client):
    response = client.get("/api/v1/legal-db/search?q=cerai")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    # Divorce-related references should be returned
    categories = {item["category"] for item in data}
    assert "perceraian" in categories


def test_search_requires_minimum_query_length(client):
    response = client.get("/api/v1/legal-db/search?q=a")  # 1 char < min 2
    assert response.status_code == 422


def test_search_with_limit(client):
    response = client.get("/api/v1/legal-db/search?q=hukum&limit=2")
    assert response.status_code == 200
    data = response.json()
    assert len(data) <= 2


def test_list_categories(client):
    response = client.get("/api/v1/legal-db/categories")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert "perceraian" in data
    assert "bisnis" in data
    assert "ketenagakerjaan" in data


def test_get_specific_reference(client):
    response = client.get("/api/v1/legal-db/uu-1-1974")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == "uu-1-1974"
    assert "Perkawinan" in data["law_name"]


def test_get_nonexistent_reference_returns_404(client):
    response = client.get("/api/v1/legal-db/nonexistent-ref-xyz")
    assert response.status_code == 404
    body = response.json()
    assert body["error"] is True
