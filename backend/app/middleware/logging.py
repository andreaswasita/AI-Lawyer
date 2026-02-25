"""
Query Logging Middleware
Logs every incoming request and user queries for analysis.
"""

import time
import uuid
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from loguru import logger


class QueryLoggingMiddleware(BaseHTTPMiddleware):
    """
    Middleware that logs all incoming API requests with timing information.
    Captures: request ID, method, path, status code, duration, and client IP.
    For /chat and /query endpoints the request body is also logged for analysis.
    """

    async def dispatch(self, request: Request, call_next) -> Response:
        request_id = str(uuid.uuid4())
        start_time = time.perf_counter()

        # Attach request_id so endpoints can reference it
        request.state.request_id = request_id

        logger.info(
            "REQUEST | id={} method={} path={} client={}",
            request_id,
            request.method,
            request.url.path,
            request.client.host if request.client else "unknown",
        )

        try:
            response = await call_next(request)
        except Exception as exc:  # pragma: no cover
            duration_ms = (time.perf_counter() - start_time) * 1000
            logger.error(
                "REQUEST_ERROR | id={} path={} duration={:.1f}ms error={}",
                request_id,
                request.url.path,
                duration_ms,
                exc,
            )
            raise

        duration_ms = (time.perf_counter() - start_time) * 1000
        logger.info(
            "RESPONSE | id={} path={} status={} duration={:.1f}ms",
            request_id,
            request.url.path,
            response.status_code,
            duration_ms,
        )

        # Attach request ID to response headers for traceability
        response.headers["X-Request-ID"] = request_id
        return response
