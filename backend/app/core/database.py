"""
Database Setup
Async SQLAlchemy engine and session factory.
Uses DATABASE_URL from settings (PostgreSQL in production, SQLite for tests).
"""

from __future__ import annotations

from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.config import get_settings

settings = get_settings()


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy ORM models."""
    pass


def _resolve_url(url: str) -> str:
    """Ensure the URL uses an async-compatible driver prefix."""
    if url.startswith("postgresql://"):
        return url.replace("postgresql://", "postgresql+asyncpg://", 1)
    return url


def _make_session_factory(url: str):
    """Create a new async engine + session factory for the given URL."""
    connect_args = {}
    if url.startswith("sqlite"):
        connect_args = {"check_same_thread": False}
    eng = create_async_engine(url, echo=settings.debug, connect_args=connect_args)
    factory = async_sessionmaker(bind=eng, class_=AsyncSession, expire_on_commit=False)
    return eng, factory


# Lazily initialised — set to None until first use so tests that override
# get_db never need the production driver (asyncpg) to be installed.
_engine = None
_AsyncSessionLocal = None


def _get_factory():
    global _engine, _AsyncSessionLocal
    if _AsyncSessionLocal is None:
        url = _resolve_url(settings.database_url)
        _engine, _AsyncSessionLocal = _make_session_factory(url)
    return _AsyncSessionLocal


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """FastAPI dependency that yields an async database session."""
    factory = _get_factory()
    async with factory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
