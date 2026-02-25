def test_health(client):
    response = client.get('/api/v1/health/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert data['version'] == '1.0.0'
