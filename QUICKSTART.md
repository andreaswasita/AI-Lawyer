# 🚀 AI Lawyer - Quick Start Guide

Get your AI Lawyer platform up and running in minutes!

## Prerequisites

Before you begin, ensure you have:

- ✅ **GitHub Account** - For repository hosting
- ✅ **GitHub CLI** - Installed (`gh --version`)
- ✅ **Git** - Version control (`git --version`)
- ✅ **Node.js 18+** - For frontend (`node --version`)
- ✅ **Python 3.10+** - For backend (`python --version`)
- ✅ **Azure Account** - For cloud services (optional for local dev)
- ✅ **PostgreSQL 14+** - Database (or use Docker)
- ✅ **Redis** - Caching (or use Docker)

## 📦 Initial Setup

### Step 1: Create GitHub Repository

**Option A: Using the Setup Script (Recommended)**

```bash
# Navigate to the project directory
cd C:\Users\anwasita\AI-Lawyer

# Run the setup script
setup-github-repo.bat
```

The script will:
1. Authenticate with GitHub
2. Create a private repository named "AI-Lawyer"
3. Initialize Git
4. Make initial commit
5. Push to GitHub

**Option B: Manual Setup**

```bash
# Authenticate with GitHub CLI
gh auth login --web

# Create private repository
cd C:\Users\anwasita\AI-Lawyer
gh repo create AI-Lawyer --private --description "Democratizing Legal Services for Indonesian Citizens" --source=. --remote=origin

# Initialize and push
git init
git add .
git commit -m "Initial commit: AI Lawyer platform foundation"
git branch -M main
git push -u origin main
```

### Step 2: Clone and Setup Project

If you created the repo via web interface:

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/AI-Lawyer.git
cd AI-Lawyer

# Copy environment templates
copy backend\.env.example backend\.env
copy frontend\.env.local.example frontend\.env.local
```

### Step 3: Set Up Backend (Python/FastAPI)

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Set up database
# Create PostgreSQL database named 'ailawyer'
createdb ailawyer

# Run migrations
alembic upgrade head

# Seed initial data (optional)
python scripts/seed_data.py
```

**Configure backend/.env**:

```env
# Database
DATABASE_URL=postgresql://postgres:password@localhost:5432/ailawyer

# Azure OpenAI (for AI chatbot)
AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o

# Redis (for caching & queues)
REDIS_URL=redis://localhost:6379/0

# Security
SECRET_KEY=your_super_secret_key_here_min_32_chars
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Midtrans (Payment Gateway)
MIDTRANS_SERVER_KEY=your_midtrans_server_key
MIDTRANS_CLIENT_KEY=your_midtrans_client_key
MIDTRANS_IS_PRODUCTION=false

# Vector Database (Pinecone for legal corpus)
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENVIRONMENT=us-west1-gcp

# Email (SendGrid)
SENDGRID_API_KEY=your_sendgrid_api_key
FROM_EMAIL=noreply@hukumai.id

# Environment
ENVIRONMENT=development
DEBUG=true
```

**Start backend server**:

```bash
# Development mode with auto-reload
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Access API docs at: http://localhost:8000/docs
```

### Step 4: Set Up Frontend (Next.js/React)

Open a new terminal:

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Configure frontend/.env.local
# See configuration below
```

**Configure frontend/.env.local**:

```env
# API Configuration
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_API_TIMEOUT=30000

# Authentication
NEXTAUTH_URL=http://localhost:3000
NEXTAUTH_SECRET=your_nextauth_secret_min_32_chars

# Payment Gateway (Midtrans)
NEXT_PUBLIC_MIDTRANS_CLIENT_KEY=your_midtrans_client_key
NEXT_PUBLIC_MIDTRANS_ENVIRONMENT=sandbox

# Analytics (optional)
NEXT_PUBLIC_GA_MEASUREMENT_ID=G-XXXXXXXXXX
NEXT_PUBLIC_MIXPANEL_TOKEN=your_mixpanel_token

# Feature Flags
NEXT_PUBLIC_ENABLE_CHAT=true
NEXT_PUBLIC_ENABLE_DOCUMENT_GENERATION=true
NEXT_PUBLIC_ENABLE_LAWYER_BOOKING=true
NEXT_PUBLIC_ENABLE_VIDEO_CONSULTATION=false

# Environment
NEXT_PUBLIC_ENVIRONMENT=development
```

**Start frontend development server**:

```bash
npm run dev

# Access web app at: http://localhost:3000
```

### Step 5: Set Up Services (Docker)

**Option A: Using Docker Compose (Recommended for Local Development)**

```bash
# In project root directory
cd C:\Users\anwasita\AI-Lawyer

# Start all services (PostgreSQL, Redis, Backend, Frontend)
docker-compose up -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down
```

**Option B: Manual Service Installation**

**PostgreSQL**:
```bash
# Download and install: https://www.postgresql.org/download/
# Or use Azure Database for PostgreSQL

# Create database
psql -U postgres
CREATE DATABASE ailawyer;
CREATE USER ailawyer_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE ailawyer TO ailawyer_user;
\q
```

**Redis**:
```bash
# Download and install: https://redis.io/download
# Or use Azure Cache for Redis

# Start Redis server
redis-server
```

## 🧪 Running Tests

### Backend Tests

```bash
cd backend

# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_api/test_chat.py

# View coverage report
# Open htmlcov/index.html in browser
```

### Frontend Tests

```bash
cd frontend

# Run unit tests
npm test

# Run with coverage
npm test -- --coverage

# Run E2E tests (Playwright)
npx playwright test

# View test report
npx playwright show-report
```

## 🔍 Verify Installation

### Check Backend API

```bash
# Health check
curl http://localhost:8000/health

# Expected response:
# {"status": "healthy", "version": "0.1.0"}

# API documentation
# Open: http://localhost:8000/docs
```

### Check Frontend

```bash
# Open browser: http://localhost:3000

# You should see the AI Lawyer home page
```

### Check Database Connection

```bash
# Connect to PostgreSQL
psql -U postgres -d ailawyer

# List tables
\dt

# You should see: users, documents, lawyers, consultations, etc.
```

### Check AI Chatbot

```bash
# Test AI endpoint
curl -X POST http://localhost:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Apa itu perceraian?", "language": "id"}'

# Expected: AI response in Bahasa Indonesia
```

## 🎨 Development Workflow

### 1. Create a Feature Branch

```bash
git checkout -b feature/document-generation
```

### 2. Make Changes

```bash
# Edit files
# Run tests
npm test  # or pytest

# Lint code
npm run lint  # or black . && flake8
```

### 3. Commit Changes

```bash
git add .
git commit -m "feat: add rental agreement document template"
```

### 4. Push and Create PR

```bash
git push origin feature/document-generation

# Create PR on GitHub
gh pr create --title "Add rental agreement template" --body "Implements document generation for rental agreements"
```

### 5. Code Review & Merge

- Wait for CI checks to pass
- Request review from team members
- Address feedback
- Merge to `main` branch

## 📚 Next Steps

### For Developers

1. **Read the Documentation**
   - [Full Research & Business Plan](./docs/RESEARCH.md)
   - [Technical Architecture](./docs/ARCHITECTURE.md)
   - [API Documentation](./docs/API.md)
   - [Contribution Guidelines](./CONTRIBUTING.md)

2. **Set Up Development Tools**
   - Install VS Code extensions: Python, Prettier, ESLint, Tailwind CSS IntelliSense
   - Configure IDE settings for TypeScript and Python
   - Set up Git hooks for pre-commit linting

3. **Explore the Codebase**
   - Review [Project Structure](./PROJECT_STRUCTURE.md)
   - Understand the AI chatbot logic in `backend/app/ai/`
   - Explore frontend components in `frontend/src/components/`

4. **Implement Your First Feature**
   - Pick an issue tagged `good first issue`
   - Follow the [Contributing Guide](./CONTRIBUTING.md)
   - Submit your first PR!

### For Legal Experts

1. **Review Legal Templates**
   - Check `legal-corpus/templates/` directory
   - Validate accuracy of legal documents
   - Suggest improvements for plain language

2. **Build Legal Knowledge Base**
   - Contribute Indonesian legal texts
   - Add case precedents
   - Write legal guides in Bahasa Indonesia

3. **Join as a Lawyer Partner**
   - Register in the lawyer network (coming in Phase 2)
   - Provide consultations to users
   - Review AI-generated documents

### For Product/Business

1. **User Research**
   - Interview potential Indonesian users
   - Validate pricing assumptions
   - Test product-market fit

2. **Partnerships**
   - Connect with Indonesian Bar Association (PERADI)
   - Partner with legal aid organizations
   - Explore insurance company integrations

3. **Go-to-Market Strategy**
   - Plan marketing campaigns
   - Create educational content
   - Build community on social media

## 🆘 Troubleshooting

### Backend won't start

```bash
# Check Python version
python --version  # Should be 3.10+

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall

# Check database connection
psql -U postgres -d ailawyer -c "SELECT 1;"

# Check environment variables
cat backend/.env
```

### Frontend won't start

```bash
# Check Node version
node --version  # Should be 18+

# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install

# Check environment variables
cat frontend/.env.local
```

### AI chatbot not responding

```bash
# Verify Azure OpenAI credentials
curl -X GET https://your-resource.openai.azure.com/openai/deployments \
  -H "api-key: YOUR_API_KEY"

# Check if embeddings are loaded
curl http://localhost:8000/api/v1/health/ai

# Re-index legal corpus
python backend/scripts/reindex_corpus.py
```

### Database migration errors

```bash
# Reset database (WARNING: Deletes all data)
dropdb ailawyer
createdb ailawyer
alembic upgrade head

# Or rollback and re-migrate
alembic downgrade base
alembic upgrade head
```

## 🔗 Useful Links

- **GitHub Repository**: https://github.com/YOUR_USERNAME/AI-Lawyer
- **API Documentation**: http://localhost:8000/docs (when running locally)
- **Frontend**: http://localhost:3000 (when running locally)
- **Project Board**: https://github.com/YOUR_USERNAME/AI-Lawyer/projects
- **Issues**: https://github.com/YOUR_USERNAME/AI-Lawyer/issues
- **Discussions**: https://github.com/YOUR_USERNAME/AI-Lawyer/discussions

## 📞 Get Help

- **GitHub Discussions**: For questions and ideas
- **GitHub Issues**: For bug reports and feature requests
- **Email**: dev@hukumai.id
- **Discord**: Coming soon!

---

**Congratulations! You're ready to start building AI Lawyer!** 🎉

*Hukum untuk Semua* (Law for Everyone) 🇮🇩⚖️
