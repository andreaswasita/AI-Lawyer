"""
AI Lawyer Backend - Configuration
Loads environment variables and provides typed settings
"""

from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""

    # Application
    app_name: str = "AI-Lawyer"
    app_version: str = "0.1.0"
    app_env: str = "development"
    debug: bool = True
    secret_key: str = "change-me-in-production"
    api_prefix: str = "/api/v1"

    # Server
    host: str = "0.0.0.0"
    port: int = 8000

    # Database
    database_url: str = "postgresql+asyncpg://postgres:password@localhost:5432/ailawyer"
    database_url_sync: str = "postgresql://postgres:password@localhost:5432/ailawyer"

    # Redis
    redis_url: str = "redis://localhost:6379/0"

    # Azure OpenAI
    azure_openai_api_key: str = ""
    azure_openai_endpoint: str = ""
    azure_openai_deployment: str = "gpt-4o"
    azure_openai_api_version: str = "2024-08-01-preview"
    azure_openai_embedding_deployment: str = "text-embedding-3-large"

    # Qdrant
    qdrant_host: str = "localhost"
    qdrant_port: int = 6333
    qdrant_collection: str = "indonesian_law"

    # JWT
    jwt_secret_key: str = "change-me-in-production"
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 30
    jwt_refresh_token_expire_days: int = 7

    # Midtrans
    midtrans_server_key: str = ""
    midtrans_client_key: str = ""
    midtrans_is_production: bool = False
    midtrans_merchant_id: str = ""

    # Rate Limiting (questions per day)
    rate_limit_free: int = 5
    rate_limit_starter: int = 50
    rate_limit_pro: int = 200
    rate_limit_business: int = 1000

    # CORS
    cors_origins: str = "http://localhost:3000,http://localhost:8000"

    # Sentry
    sentry_dsn: Optional[str] = None

    # Logging
    log_level: str = "DEBUG"

    @property
    def cors_origins_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",")]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance"""
    return Settings()
