# ai_service.py
# This file is responsible ONLY for communicating with the Google Gemini AI.
# It sends a prompt and returns the raw text response.
# It does NOT build prompts, parse JSON, or implement quiz logic.

import google.generativeai as genai

from app.core.config import settings
from app.core.logger import logger

# Configure the Gemini client using the API key from settings
genai.configure(api_key=settings.GEMINI_API_KEY)


class AIService:
    """
    Service class responsible for communicating with the Gemini AI model.
    """

    def __init__(self):
        # Create the Gemini model instance using the model name from config
        self.model = genai.GenerativeModel(settings.GEMINI_MODEL_NAME)

    def generate_content(self, prompt: str) -> str:
        """
        Sends the given prompt to the Gemini model and returns the raw text response.

        Parameters:
            prompt (str): The prompt string to send to the AI model.

        Returns:
            str: The raw text response from the AI model.
        """
        try:
            # Log that the request is being sent
            logger.info("Sending request to Gemini AI model")

            # Send the prompt to the Gemini model
            response = self.model.generate_content(prompt)

            # Log successful response
            logger.info("Response received successfully from Gemini AI model")

            # Return only the raw text from the response
            return response.text

        except Exception as e:
            # Log the error with details
            logger.error(f"Error occurred while communicating with Gemini AI: {e}")

            # Re-raise the exception so the caller can handle it
            raise