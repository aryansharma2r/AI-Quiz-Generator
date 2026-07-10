# main.py
# This is the entry point of the AI Quiz Generator FastAPI application.
# It creates the FastAPI app, sets up basic metadata, includes routers,
# and logs a startup message.

from fastapi import FastAPI

from app.core.config import settings
from app.core.logger import logger
from app.api.health import router as health_router
from app.api.quiz import router as quiz_router

# Create the FastAPI application instance
# title and version are shown in Swagger UI (/docs)
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

# Include the health check router
# This makes the /health endpoint available in the app
app.include_router(health_router)

# Include the quiz router
# This makes the /generate-quiz endpoint available in the app
app.include_router(quiz_router)

# Log a message to confirm the application has started successfully
logger.info(f"{settings.APP_NAME} v{settings.APP_VERSION} started successfully")


@app.get("/", summary="Root Endpoint", description="Basic welcome message for the API.")
def read_root():
    """
    Root endpoint.
    Returns a simple welcome message.
    """
    return {
        "message": "Welcome to AI Quiz Generator API"
    }
