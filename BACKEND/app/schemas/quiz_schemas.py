# quiz_schema.py
# This file defines the structured schema for a single quiz question
# and the overall quiz containing multiple questions.
# These models represent the structured shape of AI-generated quiz data.

from pydantic import BaseModel, Field
from typing import List


class Question(BaseModel):
    """
    Schema representing a single quiz question.
    """

    # The actual question text
    question: str = Field(
        ...,
        description="The quiz question text"
    )

    # List of answer options for the question
    options: List[str] = Field(
        ...,
        description="List of possible answer options for the question"
    )

    # The correct answer among the options
    correct_answer: str = Field(
        ...,
        description="The correct answer for the question"
    )


class QuizSchema(BaseModel):
    """
    Schema representing the full quiz, containing a list of questions.
    """

    # List of Question objects that make up the quiz
    questions: List[Question] = Field(
        ...,
        description="List of quiz questions"
    )