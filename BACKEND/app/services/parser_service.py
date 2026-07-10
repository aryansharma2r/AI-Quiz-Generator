# parser_service.py
# This file is responsible ONLY for parsing raw JSON text
# (returned by the AI) into a Python dictionary.
# It does NOT validate fields, modify data, or add business logic.

import json

from app.core.logger import logger


class ParserService:
    """
    Service class responsible for parsing raw JSON text into a Python dictionary.
    """

    def parse_json(self, response_text: str) -> dict:
        """
        Parses the raw text response from the AI into a Python dictionary.

        Parameters:
            response_text (str): The raw JSON text returned by the AI.

        Returns:
            dict: The parsed JSON data as a Python dictionary.
        """
        try:
            # Log that parsing has started
            logger.info("Parsing started for AI response text")

            # Convert the raw JSON string into a Python dictionary
            parsed_data = json.loads(response_text)

            # Log successful parsing
            logger.info("Parsing successful")

            # Return the parsed dictionary
            return parsed_data

        except Exception as e:
            # Log the parsing error with details
            logger.error(f"Parsing failed: {e}")

            # Re-raise the exception so the caller can handle it
            raise
        