# quiz_service.py
# This file coordinates the quiz generation process by combining
# the prompt builder, AI service, and parser service together.
# It does NOT validate data, build API responses, or contain business logic.

from app.core.prompt import build_quiz_prompt
from app.core.logger import logger
from app.services.ai_service import AIService
from app.services.parser_service import ParserService


class QuizService:
    """
    Service class responsible for coordinating quiz generation
    using the prompt builder, AI service, and parser service.
    """

    def __init__(self):
        # Create instances of the AI service and parser service
        self.ai_service = AIService()
        self.parser_service = ParserService()

    def generate_quiz(self, topic: str, difficulty: str, question_count: int, question_type: str) -> dict:
        """
        Coordinates the full quiz generation flow:
        build prompt -> call AI -> parse response.

        Parameters:
            topic (str): Topic for the quiz.
            difficulty (str): Difficulty level of the quiz.
            question_count (int): Number of questions to generate.
            question_type (str): Type of questions (e.g. MCQ, True/False).

        Returns:
            dict: The parsed quiz data.
        """
        try:
            # Step 1: Build the prompt using the prompt builder
            prompt = build_quiz_prompt(topic, difficulty, question_count, question_type)

            # Step 2: Log that quiz generation has started
            logger.info("Quiz generation started")

            # Step 3: Send the prompt to the AI service and get raw text response
            response_text = self.ai_service.generate_content(prompt)

            # Step 4: Parse the raw text response into a dictionary
            parsed_data = self.parser_service.parse_json(response_text)

            # Step 5: Log successful quiz generation
            logger.info("Quiz generated successfully")

            # Step 6: Return the parsed dictionary
            return parsed_data

        except Exception as e:
            # Log the error with details
            logger.error(f"Quiz generation failed: {e}")

            # Re-raise the exception so the caller (API layer) can handle it
            raise