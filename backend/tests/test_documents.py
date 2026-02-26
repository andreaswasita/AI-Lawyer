"""
Unit tests for the document generation endpoints.
"""


def test_generate_document_returns_response(client):
    payload = {
        "template_id": "surat-gugatan-cerai",
        "fields": {
            "nama_penggugat": "Siti Nurhaliza",
            "nama_tergugat": "Ahmad Dahlan",
            "alamat_penggugat": "Jl. Sudirman No. 100, Jakarta Selatan",
            "alamat_tergugat": "Jl. Gatot Subroto No. 50, Jakarta Selatan",
            "alasan_cerai": "Tidak ada keharmonisan dalam rumah tangga",
        },
        "language": "id",
        "format": "docx",
    }
    response = client.post("/api/v1/documents/generate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "document_id" in data
    assert data["template_id"] == "surat-gugatan-cerai"
    assert "preview_text" in data
    assert data["status"] == "generated"


def test_generate_document_requires_template_id(client):
    payload = {"fields": {}, "language": "id", "format": "docx"}
    response = client.post("/api/v1/documents/generate", json=payload)
    assert response.status_code == 422


def test_list_documents_returns_empty_initially(client):
    response = client.get("/api/v1/documents/")
    assert response.status_code == 200
    data = response.json()
    assert "documents" in data
    assert "total" in data


def test_get_nonexistent_document_returns_404(client):
    response = client.get("/api/v1/documents/nonexistent-id")
    assert response.status_code == 404
    body = response.json()
    assert body["error"] is True
