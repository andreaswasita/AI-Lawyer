from unittest.mock import patch

def test_chat_query_requires_auth(client):
    response = client.post('/api/v1/chat/query', json={'query': 'test'})
    assert response.status_code == 401

def test_chat_query(client, db):
    reg = client.post('/api/v1/auth/register',
        json={'email': 'chat@example.com', 'password': 'password123', 'name': 'Chat User'})
    token = reg.get_json()['data']['access_token']
    
    with patch('app.services.ai_service.AIService.query') as mock_query:
        mock_query.return_value = {
            'response': 'This is a legal response.',
            'confidence': 0.95,
            'disclaimer': 'Not legal advice.'
        }
        response = client.post('/api/v1/chat/query',
            headers={'Authorization': f'Bearer {token}'},
            json={'query': 'What is contract law?'})
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True
    assert 'response' in data['data']

def test_chat_history_requires_auth(client):
    response = client.get('/api/v1/chat/history')
    assert response.status_code == 401
