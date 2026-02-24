# AI Lawyer - Project Structure

```
AI-Lawyer/
├── README.md                          # Main project documentation
├── LICENSE                            # MIT License
├── CONTRIBUTING.md                    # Contribution guidelines
├── .gitignore                        # Git ignore rules
├── docker-compose.yml                # Local development environment
├── .github/                          # GitHub configuration
│   ├── workflows/                    # CI/CD pipelines
│   │   ├── backend-ci.yml           # Backend tests & deployment
│   │   ├── frontend-ci.yml          # Frontend tests & deployment
│   │   └── security-scan.yml        # Security vulnerability scanning
│   ├── ISSUE_TEMPLATE/              # Issue templates
│   └── PULL_REQUEST_TEMPLATE.md     # PR template
│
├── docs/                             # Documentation
│   ├── RESEARCH.md                   # Market research & business plan
│   ├── ARCHITECTURE.md               # Technical architecture
│   ├── API.md                        # API documentation
│   ├── DEPLOYMENT.md                 # Deployment guide
│   ├── SECURITY.md                   # Security practices
│   └── images/                       # Diagrams & screenshots
│
├── backend/                          # Backend API (FastAPI/Python)
│   ├── README.md
│   ├── requirements.txt              # Python dependencies
│   ├── requirements-dev.txt          # Dev dependencies
│   ├── alembic.ini                   # Database migrations config
│   ├── pytest.ini                    # Test configuration
│   ├── Dockerfile                    # Backend container
│   ├── .env.example                  # Environment template
│   │
│   ├── alembic/                      # Database migrations
│   │   ├── env.py
│   │   └── versions/
│   │
│   ├── app/                          # Main application
│   │   ├── __init__.py
│   │   ├── main.py                   # FastAPI app entry point
│   │   ├── config.py                 # Configuration
│   │   ├── database.py               # Database connection
│   │   ├── dependencies.py           # Dependency injection
│   │   │
│   │   ├── models/                   # SQLAlchemy models
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── document.py
│   │   │   ├── lawyer.py
│   │   │   ├── consultation.py
│   │   │   └── payment.py
│   │   │
│   │   ├── schemas/                  # Pydantic schemas
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── document.py
│   │   │   ├── lawyer.py
│   │   │   └── chat.py
│   │   │
│   │   ├── api/                      # API routes
│   │   │   ├── __init__.py
│   │   │   ├── v1/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── auth.py           # Authentication endpoints
│   │   │   │   ├── chat.py           # AI chatbot endpoints
│   │   │   │   ├── documents.py      # Document generation
│   │   │   │   ├── lawyers.py        # Lawyer network
│   │   │   │   ├── consultations.py  # Video consultations
│   │   │   │   └── payments.py       # Payment processing
│   │   │
│   │   ├── services/                 # Business logic
│   │   │   ├── __init__.py
│   │   │   ├── ai_service.py         # LLM integration
│   │   │   ├── document_service.py   # Document generation
│   │   │   ├── lawyer_service.py     # Lawyer matching
│   │   │   ├── payment_service.py    # Payment processing
│   │   │   └── notification_service.py
│   │   │
│   │   ├── ai/                       # AI/ML modules
│   │   │   ├── __init__.py
│   │   │   ├── chatbot.py            # Chatbot logic
│   │   │   ├── rag.py                # RAG system
│   │   │   ├── document_generator.py # Template filling
│   │   │   ├── legal_ner.py          # Named entity recognition
│   │   │   └── embeddings.py         # Vector embeddings
│   │   │
│   │   ├── utils/                    # Utility functions
│   │   │   ├── __init__.py
│   │   │   ├── security.py           # Password hashing, JWT
│   │   │   ├── validators.py         # Input validation
│   │   │   ├── logger.py             # Logging config
│   │   │   └── exceptions.py         # Custom exceptions
│   │   │
│   │   └── workers/                  # Background tasks
│   │       ├── __init__.py
│   │       ├── celery_app.py         # Celery configuration
│   │       └── tasks.py              # Async tasks
│   │
│   └── tests/                        # Backend tests
│       ├── __init__.py
│       ├── conftest.py               # Test fixtures
│       ├── test_api/
│       ├── test_services/
│       └── test_ai/
│
├── frontend/                         # Frontend (Next.js/React)
│   ├── README.md
│   ├── package.json
│   ├── tsconfig.json
│   ├── next.config.js
│   ├── tailwind.config.js
│   ├── Dockerfile
│   ├── .env.local.example
│   │
│   ├── public/                       # Static files
│   │   ├── images/
│   │   ├── fonts/
│   │   └── locales/                  # i18n translations
│   │       ├── id/                   # Bahasa Indonesia
│   │       └── en/                   # English
│   │
│   ├── src/
│   │   ├── app/                      # Next.js 14 App Router
│   │   │   ├── layout.tsx
│   │   │   ├── page.tsx              # Home page
│   │   │   ├── (auth)/               # Auth routes
│   │   │   │   ├── login/
│   │   │   │   ├── register/
│   │   │   │   └── reset-password/
│   │   │   ├── dashboard/            # User dashboard
│   │   │   ├── chat/                 # AI chatbot interface
│   │   │   ├── documents/            # Document management
│   │   │   ├── lawyers/              # Lawyer directory
│   │   │   ├── consultations/        # Video consultations
│   │   │   ├── pricing/              # Pricing page
│   │   │   └── api/                  # API routes (Next.js)
│   │   │
│   │   ├── components/               # React components
│   │   │   ├── ui/                   # Base UI components
│   │   │   │   ├── button.tsx
│   │   │   │   ├── input.tsx
│   │   │   │   ├── card.tsx
│   │   │   │   └── ...
│   │   │   ├── layout/
│   │   │   │   ├── Header.tsx
│   │   │   │   ├── Footer.tsx
│   │   │   │   └── Sidebar.tsx
│   │   │   ├── chat/
│   │   │   │   ├── ChatInterface.tsx
│   │   │   │   ├── ChatMessage.tsx
│   │   │   │   └── ChatInput.tsx
│   │   │   ├── documents/
│   │   │   │   ├── DocumentGenerator.tsx
│   │   │   │   ├── DocumentPreview.tsx
│   │   │   │   └── DocumentList.tsx
│   │   │   └── lawyers/
│   │   │       ├── LawyerCard.tsx
│   │   │       ├── LawyerProfile.tsx
│   │   │       └── BookingForm.tsx
│   │   │
│   │   ├── lib/                      # Utility libraries
│   │   │   ├── api.ts                # API client
│   │   │   ├── auth.ts               # Auth utilities
│   │   │   ├── utils.ts              # Helper functions
│   │   │   └── constants.ts
│   │   │
│   │   ├── hooks/                    # Custom React hooks
│   │   │   ├── useAuth.ts
│   │   │   ├── useChat.ts
│   │   │   ├── useDocument.ts
│   │   │   └── useLawyer.ts
│   │   │
│   │   ├── store/                    # State management (Zustand)
│   │   │   ├── authStore.ts
│   │   │   ├── chatStore.ts
│   │   │   └── documentStore.ts
│   │   │
│   │   ├── types/                    # TypeScript types
│   │   │   ├── index.ts
│   │   │   ├── api.ts
│   │   │   └── models.ts
│   │   │
│   │   └── styles/                   # Global styles
│   │       ├── globals.css
│   │       └── themes.css
│   │
│   └── tests/                        # Frontend tests
│       ├── e2e/                      # End-to-end tests
│       └── unit/                     # Unit tests
│
├── mobile/                           # Mobile App (React Native)
│   ├── README.md
│   ├── package.json
│   ├── app.json
│   ├── babel.config.js
│   ├── metro.config.js
│   │
│   ├── src/
│   │   ├── App.tsx
│   │   ├── navigation/
│   │   ├── screens/
│   │   ├── components/
│   │   ├── services/
│   │   ├── hooks/
│   │   └── utils/
│   │
│   ├── ios/                          # iOS native code
│   └── android/                      # Android native code
│
├── infrastructure/                   # Infrastructure as Code
│   ├── azure/                        # Azure Bicep templates
│   │   ├── main.bicep
│   │   ├── app-service.bicep
│   │   ├── database.bicep
│   │   ├── storage.bicep
│   │   ├── front-door.bicep
│   │   └── parameters/
│   │       ├── dev.parameters.json
│   │       ├── staging.parameters.json
│   │       └── production.parameters.json
│   │
│   ├── kubernetes/                   # K8s manifests (if scaling)
│   │   ├── deployments/
│   │   ├── services/
│   │   └── ingress/
│   │
│   └── scripts/                      # Deployment scripts
│       ├── deploy.sh
│       ├── rollback.sh
│       └── migrate.sh
│
├── legal-corpus/                     # Legal knowledge base
│   ├── README.md
│   ├── laws/                         # Indonesian laws (Undang-Undang)
│   ├── regulations/                  # Government regulations
│   ├── precedents/                   # Court decisions
│   ├── templates/                    # Legal document templates
│   │   ├── property/
│   │   ├── family/
│   │   ├── business/
│   │   ├── employment/
│   │   └── wills/
│   └── scripts/                      # Scraping & processing scripts
│       ├── scrape_laws.py
│       └── process_corpus.py
│
├── data/                             # Data & analytics
│   ├── migrations/                   # Database migrations
│   ├── seeds/                        # Seed data
│   └── analytics/                    # Analytics queries
│
└── scripts/                          # Utility scripts
    ├── setup.sh                      # Initial setup script
    ├── test.sh                       # Run all tests
    ├── lint.sh                       # Linting
    ├── backup.sh                     # Database backup
    └── deploy.sh                     # Deployment wrapper
```

## Key Directories Explained

### `/backend` - Backend API
FastAPI-based REST API handling:
- User authentication & authorization
- AI chatbot interactions
- Document generation
- Lawyer network management
- Payment processing
- Background jobs (email, notifications)

### `/frontend` - Web Application
Next.js 14 web app with:
- Server-side rendering for SEO
- AI chatbot interface
- Document generation wizard
- Lawyer booking system
- User dashboard
- Payment integration

### `/mobile` - Mobile Apps
React Native app for iOS & Android with native features:
- Push notifications
- Biometric authentication
- Offline document viewing
- Camera integration (document scanning)

### `/legal-corpus` - Legal Knowledge Base
Curated collection of:
- Indonesian laws & regulations
- Legal precedents & case law
- Document templates
- Legal guides in plain language

### `/infrastructure` - IaC & DevOps
Azure infrastructure definitions:
- App Services (backend API)
- Azure Front Door (CDN & WAF)
- PostgreSQL database
- Blob Storage (documents)
- Application Insights (monitoring)
- Key Vault (secrets)

## Tech Stack Summary

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend** | Next.js 14, React, TypeScript, Tailwind | Web UI |
| **Mobile** | React Native | iOS/Android apps |
| **Backend** | FastAPI, Python 3.11 | REST API |
| **Database** | PostgreSQL 15 | Relational data |
| **Vector DB** | Pinecone/Qdrant | Legal corpus RAG |
| **Cache** | Redis | Session & caching |
| **Queue** | Celery | Background tasks |
| **AI/ML** | Azure OpenAI, LangChain | LLM & RAG |
| **Storage** | Azure Blob Storage | Documents |
| **Auth** | Auth0/Supabase | Authentication |
| **Payment** | Midtrans | Indonesian payments |
| **Cloud** | Microsoft Azure | Infrastructure |
| **Monitoring** | Application Insights, Sentry | Observability |
| **CI/CD** | GitHub Actions | Automation |

## Getting Started

See [CONTRIBUTING.md](../CONTRIBUTING.md) for setup instructions.

## Development Workflow

1. **Local Development**: Docker Compose for all services
2. **Feature Development**: Feature branches with PR reviews
3. **Testing**: Unit, integration, E2E tests before merge
4. **Staging Deployment**: Auto-deploy from `develop` branch
5. **Production Deployment**: Manual deploy from `main` branch

## Security Considerations

- All secrets in Azure Key Vault
- Data encryption at rest (AES-256) and in transit (TLS 1.3)
- RBAC for all API endpoints
- Rate limiting on AI endpoints
- Input sanitization & validation
- Regular security audits
- Dependency vulnerability scanning (Dependabot)

## Scalability Plan

**Phase 1** (MVP - 1,000 users):
- Single Azure App Service (B1)
- Managed PostgreSQL (Basic tier)
- Shared Redis instance

**Phase 2** (Growth - 10,000 users):
- Scale-out App Service (S1 × 2)
- PostgreSQL (General Purpose)
- Dedicated Redis (Standard)
- Azure Front Door + CDN

**Phase 3** (Scale - 100,000+ users):
- AKS (Kubernetes) cluster
- PostgreSQL (High Availability)
- Redis Cluster
- Azure Front Door Premium
- CDN + Edge computing
- Multi-region deployment

---

**Last Updated**: February 24, 2026
