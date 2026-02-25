# AI Lawyer Backend

Flask-based REST API backend for the AI Lawyer application, deployable to **Azure App Service**.

## Tech Stack
- **Framework**: Flask 3.0 + Gunicorn
- **Database**: PostgreSQL (SQLAlchemy ORM)
- **Auth**: Flask-JWT-Extended
- **AI**: Azure OpenAI (GPT-4)
- **Hosting**: Azure App Service

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure environment
```bash
cp .env.example .env
# Edit .env with your values
```

### 3. Initialize database
```bash
flask db init
flask db migrate -m "initial"
flask db upgrade
```

### 4. Run locally
```bash
FLASK_ENV=development python app.py
```

## Deploy to Azure App Service

### Using Azure CLI
```bash
az webapp up --name your-app-name --resource-group your-rg --runtime PYTHON:3.11
az webapp config set --name your-app-name --resource-group your-rg --startup-file startup.sh
```

### Environment Variables (Azure App Service)
Set these in Azure Portal > App Service > Configuration > Application Settings:
- `FLASK_ENV=production`
- `SECRET_KEY`
- `JWT_SECRET_KEY`
- `DATABASE_URL`
- `AZURE_OPENAI_API_KEY`
- `AZURE_OPENAI_ENDPOINT`
- `AZURE_OPENAI_DEPLOYMENT_NAME`

## API Endpoints

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/api/v1/auth/register` | No | Register user |
| POST | `/api/v1/auth/login` | No | Login |
| POST | `/api/v1/auth/refresh` | Refresh token | Refresh access token |
| POST | `/api/v1/auth/logout` | Yes | Logout |
| GET | `/api/v1/auth/me` | Yes | Current user |
| POST | `/api/v1/chat/query` | Yes | AI legal query |
| GET | `/api/v1/chat/history` | Yes | Chat history |
| GET | `/api/v1/documents/` | Yes | List documents |
| POST | `/api/v1/documents/generate` | Yes | Generate document |
| GET | `/api/v1/documents/<id>` | Yes | Get document |
| GET | `/api/v1/lawyers/` | Yes | List lawyers |
| GET | `/api/v1/lawyers/<id>` | Yes | Get lawyer |
| GET | `/api/v1/lawyers/search` | Yes | Search lawyers |
| GET | `/api/v1/health/` | No | Health check |

## Running Tests
```bash
cd backend
pip install pytest
pytest tests/
```
