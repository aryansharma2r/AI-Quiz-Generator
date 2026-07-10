# quiz.py
# This file defines the quiz generation endpoint.
# It uses QuizService to generate the quiz and returns the result
# in the standard response format.

from fastapi import APIRouter, HTTPException, status

from app.schemas.request import QuizRequest
from app.schemas.response import QuizResponse
from app.services.quiz_service import QuizService
from app.core.logger import logger

# Create a router for quiz-related endpoints
router = APIRouter()

# Create a single reusable instance of QuizService
quiz_service = QuizService()


@router.post(
    "/generate-quiz",
    response_model=QuizResponse,
    status_code=status.HTTP_200_OK,
    summary="Generate Quiz",
    description="Accepts quiz parameters (topic, difficulty, question count, question type), "
                "generates a quiz using AI, and returns the structured quiz data."
)
def generate_quiz(request: QuizRequest):
    """
    Quiz generation endpoint.
    Uses QuizService to build the prompt, call the AI, and parse the response.
    """
    try:
        # Call QuizService to generate the quiz using the validated request fields
        quiz_data = quiz_service.generate_quiz(
            topic=request.topic,
            difficulty=request.difficulty,
            question_count=request.question_count,
            question_type=request.question_type
        )

        # Return the successful response with the generated quiz data
        return QuizResponse(
            success=True,
            message="Quiz generated successfully",
            data=quiz_data
        )

    except Exception as e:
        # Log the error with details
        logger.error(f"Quiz generation endpoint failed: {e}")

        # Return a proper HTTP 500 error response
        raise HTTPException(
            status_code=500,
            detail="Failed to generate quiz. Please try again later."
        )