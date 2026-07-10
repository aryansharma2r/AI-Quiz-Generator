# health.py
# This file defines a simple health check endpoint.
# It is used to verify that the API is up and running.

from fastapi import APIRouter, status

# Create a router for health-related endpoints
router = APIRouter()


@router.get(
    "/health",
    status_code=status.HTTP_200_OK,
    summary="Health Check",
    description="Simple endpoint to check if the AI Quiz Generator API is running."
)
def health_check():
    """
    Health check endpoint.
    Returns a static JSON response confirming the API is healthy.
    """
    return {
        "status": "healthy",
        "message": "AI Quiz Generator API is running"
    }