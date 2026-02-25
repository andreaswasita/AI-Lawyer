"""
Global Error Handlers
Provides consistent JSON error responses for all exceptions.
"""

from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from loguru import logger


async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    """Handle FastAPI HTTP exceptions and return a structured JSON error."""
    request_id = getattr(request.state, "request_id", None)
    logger.warning(
        "HTTP_ERROR | id={} status={} detail={}",
        request_id,
        exc.status_code,
        exc.detail,
    )
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": True,
            "status_code": exc.status_code,
            "message": exc.detail,
            "request_id": request_id,
        },
    )


async def validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    """Handle Pydantic request validation errors with human-readable messages."""
    request_id = getattr(request.state, "request_id", None)
    errors = []
    for error in exc.errors():
        field = " -> ".join(str(loc) for loc in error["loc"])
        errors.append({"field": field, "message": error["msg"], "type": error["type"]})

    logger.warning(
        "VALIDATION_ERROR | id={} errors={}",
        request_id,
        errors,
    )
    return JSONResponse(
        status_code=422,
        content={
            "error": True,
            "status_code": 422,
            "message": "Request validation failed",
            "errors": errors,
            "request_id": request_id,
        },
    )


async def unhandled_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """Catch-all handler for unexpected server errors."""
    request_id = getattr(request.state, "request_id", None)
    logger.error(
        "UNHANDLED_ERROR | id={} path={} error={}",
        request_id,
        request.url.path,
        exc,
        exc_info=True,
    )
    return JSONResponse(
        status_code=500,
        content={
            "error": True,
            "status_code": 500,
            "message": "An internal server error occurred. Please try again later.",
            "request_id": request_id,
        },
    )
