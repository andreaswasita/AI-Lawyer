"""
Authentication Endpoint
Handles user registration, login, and token management using JWT + bcrypt.
"""

import uuid
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.deps import get_current_user
from app.core.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
    hash_password,
    verify_password,
)
from app.models.user import User, UserTier

router = APIRouter()


# ── Request / Response Schemas ────────────────────────────────────────────


class RegisterRequest(BaseModel):
    """User registration"""

    email: str = Field(..., description="Email address")
    password: str = Field(..., min_length=8, description="Password (min 8 characters)")
    full_name: str = Field(..., min_length=2, description="Full name")
    phone: Optional[str] = Field(None, description="Phone number (Indonesian format)")
    language: str = Field("id", description="Preferred language")

    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "user@example.com",
                "password": "securepassword123",
                "full_name": "Budi Santoso",
                "phone": "+6281234567890",
                "language": "id",
            }
        }
    }


class LoginRequest(BaseModel):
    """User login"""

    email: str
    password: str


class RefreshRequest(BaseModel):
    """Refresh token request"""

    refresh_token: str


class TokenResponse(BaseModel):
    """JWT token response"""

    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int = Field(1800, description="Token expiry in seconds")


class UserProfile(BaseModel):
    """User profile data"""

    id: str
    email: str
    full_name: str
    phone: Optional[str]
    tier: UserTier
    language: str
    questions_today: int
    questions_limit: int
    documents_generated: int
    created_at: datetime


# ── Helpers ────────────────────────────────────────────────────────────────

TIER_LIMITS = {
    UserTier.FREE: 5,
    UserTier.STARTER: 50,
    UserTier.PROFESSIONAL: 200,
    UserTier.BUSINESS: 1000,
}


def _user_to_profile(user: User) -> UserProfile:
    tier = UserTier(user.tier) if isinstance(user.tier, str) else user.tier
    return UserProfile(
        id=user.id,
        email=user.email,
        full_name=user.full_name,
        phone=user.phone,
        tier=tier,
        language=user.language,
        questions_today=user.questions_today,
        questions_limit=TIER_LIMITS.get(tier, 5),
        documents_generated=user.documents_generated,
        created_at=user.created_at,
    )


# ── Endpoints ──────────────────────────────────────────────────────────────


@router.post("/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
async def register(request: RegisterRequest, db: AsyncSession = Depends(get_db)):
    """
    Register a new user account.

    New users start on the FREE tier with:
    - 5 AI questions per day
    - 3 basic templates
    - Legal knowledge base access
    """
    # Check for duplicate email
    result = await db.execute(select(User).where(User.email == request.email))
    if result.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An account with this email already exists.",
        )

    user = User(
        id=str(uuid.uuid4()),
        email=request.email,
        hashed_password=hash_password(request.password),
        full_name=request.full_name,
        phone=request.phone,
        language=request.language,
        tier=UserTier.FREE,
    )
    db.add(user)
    await db.flush()

    token_data = {"sub": user.id}
    return TokenResponse(
        access_token=create_access_token(token_data),
        refresh_token=create_refresh_token(token_data),
        expires_in=1800,
    )


@router.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest, db: AsyncSession = Depends(get_db)):
    """Login with email and password."""
    result = await db.execute(select(User).where(User.email == request.email))
    user = result.scalar_one_or_none()

    if not user or not verify_password(request.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token_data = {"sub": user.id}
    return TokenResponse(
        access_token=create_access_token(token_data),
        refresh_token=create_refresh_token(token_data),
        expires_in=1800,
    )


@router.post("/refresh", response_model=TokenResponse)
async def refresh_token(request: RefreshRequest, db: AsyncSession = Depends(get_db)):
    """Refresh an expired access token using a valid refresh token."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired refresh token.",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_token(request.refresh_token)
        if payload.get("type") != "refresh":
            raise credentials_exception
        user_id: str = payload.get("sub")
        if not user_id:
            raise credentials_exception
    except Exception:
        raise credentials_exception

    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise credentials_exception

    token_data = {"sub": user.id}
    return TokenResponse(
        access_token=create_access_token(token_data),
        refresh_token=create_refresh_token(token_data),
        expires_in=1800,
    )


@router.get("/me", response_model=UserProfile)
async def get_profile(current_user: User = Depends(get_current_user)):
    """Get the current authenticated user's profile."""
    return _user_to_profile(current_user)


@router.post("/logout")
async def logout():
    """Logout — client should discard the JWT tokens."""
    return {"message": "Successfully logged out"}
