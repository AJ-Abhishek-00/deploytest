from fastapi.responses import JSONResponse
from fastapi import Request
import logging

logger = logging.getLogger(__name__)


async def global_exception_handler(
    request: Request,
    exc: Exception
):

    logger.error(
        f"Unhandled exception: {str(exc)}"
    )

    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "request_id": getattr(
                request.state,
                "request_id",
                None
            )
        }
    )
