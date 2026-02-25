"""AI Lawyer API v1 Package"""

from fastapi import APIRouter
from app.api.v1.endpoints import chat, documents, templates, auth, lawyers, health, legal_db

router = APIRouter()

router.include_router(health.router, prefix="/health", tags=["Health"])
router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
router.include_router(chat.router, prefix="/chat", tags=["AI Chat"])
router.include_router(documents.router, prefix="/documents", tags=["Documents"])
router.include_router(templates.router, prefix="/templates", tags=["Templates"])
router.include_router(lawyers.router, prefix="/lawyers", tags=["Lawyers"])
router.include_router(legal_db.router, prefix="/legal-db", tags=["Legal Database"])
