import json

def test_register(client, db):
    response = client.post('/api/v1/auth/register', 
        json={'email': 'test@example.com', 'password': 'password123', 'name': 'Test User'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['success'] is True
    assert 'access_token' in data['data']

def test_register_duplicate(client, db):
    client.post('/api/v1/auth/register',
        json={'email': 'dup@example.com', 'password': 'password123', 'name': 'User 1'})
    response = client.post('/api/v1/auth/register',
        json={'email': 'dup@example.com', 'password': 'password456', 'name': 'User 2'})
    assert response.status_code == 409

def test_login(client, db):
    client.post('/api/v1/auth/register',
        json={'email': 'login@example.com', 'password': 'password123', 'name': 'Login User'})
    response = client.post('/api/v1/auth/login',
        json={'email': 'login@example.com', 'password': 'password123'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True
    assert 'access_token' in data['data']

def test_login_invalid(client, db):
    response = client.post('/api/v1/auth/login',
        json={'email': 'noone@example.com', 'password': 'wrongpass'})
    assert response.status_code == 401

def test_refresh(client, db):
    reg = client.post('/api/v1/auth/register',
        json={'email': 'refresh@example.com', 'password': 'password123', 'name': 'Refresh User'})
    refresh_token = reg.get_json()['data']['refresh_token']
    response = client.post('/api/v1/auth/refresh',
        headers={'Authorization': f'Bearer {refresh_token}'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'access_token' in data['data']
