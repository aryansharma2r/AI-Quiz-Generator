# response.py
# This file defines the standard response schema for the Quiz Generator API.
# It describes the structure of the JSON response sent back to the client.

from pydantic import BaseModel, Field
from typing import Dict


class QuizResponse(BaseModel):
    """
    Schema for the outgoing API response.
    Wraps the result in a consistent success/message/data format.
    """

    # Indicates whether the request was successful
    success: bool = Field(
        ...,
        description="Indicates whether the quiz generation was successful"
    )

    # A human-readable message describing the result
    message: str = Field(
        ...,
        description="A message describing the result of the request"
    )

    # The actual quiz data, kept generic for now (dict)
    # Will be replaced/structured further using quiz_schema.py in a later phase
    data: Dict = Field(
        ...,
        description="The generated quiz data"
    )