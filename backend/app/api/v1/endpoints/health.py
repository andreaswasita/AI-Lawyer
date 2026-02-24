"""
Health Check Endpoint
"""

from fastapi import APIRouter
from datetime import datetime

router = APIRouter()


@router.get("/")
async def health():
    """Basic health check"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "AI Lawyer API",
    }


@router.get("/ready")
async def readiness():
    """Readiness check - verifies all dependencies"""
    checks = {
        "api": True,
        "database": False,  # TODO: Check DB connection
        "redis": False,  # TODO: Check Redis
        "ai_model": False,  # TODO: Check Azure OpenAI
        "vector_db": False,  # TODO: Check Qdrant
    }
    
    all_ready = all(checks.values())
    
    return {
        "ready": all_ready,
        "checks": checks,
        "timestamp": datetime.utcnow().isoformat(),
    }
