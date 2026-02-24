"""
AI Lawyer Backend - Main FastAPI Application
Hukum AI: Democratizing Legal Services for Indonesia
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from loguru import logger
import sys

from app.config import get_settings
from app.api.v1 import router as api_v1_router

settings = get_settings()

# Configure logging
logger.remove()
logger.add(
    sys.stdout,
    level=settings.log_level,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application startup and shutdown events"""
    logger.info(f"🚀 Starting {settings.app_name} v{settings.app_version}")
    logger.info(f"📍 Environment: {settings.app_env}")
    logger.info(f"🌐 CORS Origins: {settings.cors_origins_list}")
    
    # TODO: Initialize database connection pool
    # TODO: Initialize Redis connection
    # TODO: Initialize Qdrant vector store
    # TODO: Load AI models
    
    yield
    
    logger.info(f"👋 Shutting down {settings.app_name}")
    # TODO: Cleanup connections


app = FastAPI(
    title="AI Lawyer API (Hukum AI)",
    description="""
    🇮🇩⚖️ Democratizing Legal Services for Indonesian Citizens
    
    AI Lawyer provides:
    - 🤖 AI Legal Chatbot (Bahasa Indonesia)
    - 📄 Automated Document Generation
    - 👨‍⚖️ Lawyer Network Connection
    - 📚 Indonesian Legal Knowledge Base
    
    **Note:** This platform provides legal information and document automation.
    It is NOT a law firm and does NOT provide legal advice.
    For legal advice, please consult with a licensed advocate (Advokat).
    """,
    version=settings.app_version,
    docs_url="/docs" if settings.debug else None,
    redoc_url="/redoc" if settings.debug else None,
    lifespan=lifespan,
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routers
app.include_router(api_v1_router, prefix=settings.api_prefix)


@app.get("/", tags=["Health"])
async def root():
    """Root endpoint - Health check"""
    return {
        "name": settings.app_name,
        "version": settings.app_version,
        "status": "healthy",
        "environment": settings.app_env,
        "message": "Selamat datang di AI Lawyer API! 🇮🇩⚖️",
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """Detailed health check endpoint"""
    return {
        "status": "healthy",
        "services": {
            "api": "up",
            "database": "not_configured",  # TODO: Check DB connection
            "redis": "not_configured",  # TODO: Check Redis connection
            "ai_model": "not_configured",  # TODO: Check AI model
            "vector_db": "not_configured",  # TODO: Check Qdrant
        },
    }
