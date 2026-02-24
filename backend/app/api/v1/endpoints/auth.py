"""
Authentication Endpoint
Handles user registration, login, and token management
"""

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime
from enum import Enum
import uuid

router = APIRouter()


class UserTier(str, Enum):
    FREE = "free"
    STARTER = "starter"
    PROFESSIONAL = "professional"
    BUSINESS = "business"


class RegisterRequest(BaseModel):
    """User registration"""
    email: str = Field(..., description="Email address")
    password: str = Field(..., min_length=8, description="Password (min 8 characters)")
    full_name: str = Field(..., min_length=2, description="Full name")
    phone: Optional[str] = Field(None, description="Phone number (Indonesian format)")
    language: str = Field("id", description="Preferred language")

    class Config:
        json_schema_extra = {
            "example": {
                "email": "user@example.com",
                "password": "securepassword123",
                "full_name": "Budi Santoso",
                "phone": "+6281234567890",
                "language": "id",
            }
        }


class LoginRequest(BaseModel):
    """User login"""
    email: str
    password: str


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


# ── Endpoints ──────────────────────────────────────────────────────────────

@router.post("/register", response_model=TokenResponse)
async def register(request: RegisterRequest):
    """
    Register a new user account.
    
    New users start on the FREE tier with:
    - 5 AI questions per day
    - 3 basic templates
    - Legal knowledge base access
    """
    # TODO: In production:
    # 1. Check if email already exists
    # 2. Hash password with bcrypt
    # 3. Create user in PostgreSQL
    # 4. Generate JWT tokens
    # 5. Send verification email
    
    user_id = str(uuid.uuid4())
    
    return TokenResponse(
        access_token=f"demo_access_token_{user_id}",
        refresh_token=f"demo_refresh_token_{user_id}",
        token_type="bearer",
        expires_in=1800,
    )


@router.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest):
    """Login with email and password"""
    # TODO: Validate credentials against database
    
    return TokenResponse(
        access_token="demo_access_token",
        refresh_token="demo_refresh_token",
        token_type="bearer",
        expires_in=1800,
    )


@router.post("/refresh", response_model=TokenResponse)
async def refresh_token(refresh_token: str):
    """Refresh an expired access token"""
    # TODO: Validate refresh token and issue new pair
    
    return TokenResponse(
        access_token="demo_new_access_token",
        refresh_token="demo_new_refresh_token",
        token_type="bearer",
        expires_in=1800,
    )


@router.get("/me", response_model=UserProfile)
async def get_profile():
    """Get current user's profile"""
    # TODO: Extract user from JWT token and query database
    
    return UserProfile(
        id="demo-user-id",
        email="demo@ailawyer.id",
        full_name="Demo User",
        phone="+6281234567890",
        tier=UserTier.FREE,
        language="id",
        questions_today=2,
        questions_limit=5,
        documents_generated=0,
        created_at=datetime.utcnow(),
    )


@router.post("/logout")
async def logout():
    """Logout and invalidate tokens"""
    # TODO: Blacklist the JWT token
    return {"message": "Successfully logged out"}
