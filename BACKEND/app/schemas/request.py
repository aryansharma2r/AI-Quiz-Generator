# request.py
# This file defines the request schema for the Quiz Generator API.
# It describes what data the client must send when requesting a quiz.

from pydantic import BaseModel, Field


class QuizRequest(BaseModel):
    """
    Schema for the incoming quiz generation request.
    Defines the fields the client must provide.
    """

    # Topic on which the quiz should be generated (e.g. "Python", "History")
    topic: str = Field(
        ...,
        description="The topic on which the quiz should be generated"
    )

    # Difficulty level of the quiz (e.g. "easy", "medium", "hard")
    difficulty: str = Field(
        ...,
        description="Difficulty level of the quiz"
    )

    # Number of questions to generate, must be greater than 0
    question_count: int = Field(
        ...,
        gt=0,
        description="Number of quiz questions to generate (must be greater than 0)"
    )

    # Type of questions (e.g. "MCQ", "True/False")
    question_type: str = Field(
        ...,
        description="Type of quiz questions (e.g. MCQ, True/False)"
    )