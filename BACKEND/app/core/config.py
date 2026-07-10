# config.py
# This file loads environment variables and provides a single place
# to access all configuration values used across the project.

import os
from dotenv import load_dotenv

# Load variables from the .env file into the environment
load_dotenv()


class Settings:
    """
    Simple configuration class.
    Reads values from environment variables (loaded via .env)
    and exposes them as easy-to-use attributes.
    """

    # Gemini API Key - used to authenticate with Google Gemini API
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")

    # Gemini Model Name - which Gemini model to use for generation
    GEMINI_MODEL_NAME: str = os.getenv("GEMINI_MODEL_NAME", "gemini-2.5-flash")

    # Application Name - shown in FastAPI docs / Swagger UI
    APP_NAME: str = os.getenv("APP_NAME", "AI Quiz Generator")

    # Application Version - shown in FastAPI docs / Swagger UI
    APP_VERSION: str = os.getenv("APP_VERSION", "1.0.0")


# Create a single reusable settings instance.
# Other files will import this object to access configuration values.
settings = Settings()