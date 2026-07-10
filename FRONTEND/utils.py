# utils.py
# This file is responsible ONLY for communicating with the FastAPI backend.
# It sends quiz requests and returns the response as a dictionary.

import json
import urllib.request
import urllib.error

# Some environments (linters/IDEs) may report `requests` as unresolved.
# Try to import requests and fall back to urllib if it's not available.
try:
    import requests
    _HAS_REQUESTS = True
except Exception:
    requests = None
    _HAS_REQUESTS = False

# Backend endpoint URL for quiz generation
BACKEND_URL = "http://127.0.0.1:8000/generate-quiz"


def generate_quiz(topic: str, difficulty: str, question_count: int, question_type: str) -> dict:
    """
    Sends a quiz generation request to the FastAPI backend.

    Parameters:
        topic (str): The topic for the quiz.
        difficulty (str): Difficulty level of the quiz.
        question_count (int): Number of questions to generate.
        question_type (str): Type of questions (e.g. MCQ, True/False).

    Returns:
        dict: The JSON response from the backend, or a fallback error dict
              if the request fails.
    """
    # Build the request payload matching the backend's QuizRequest schema
    payload = {
        "topic": topic,
        "difficulty": difficulty,
        "question_count": question_count,
        "question_type": question_type
    }

    if _HAS_REQUESTS:
        try:
            # Send a POST request to the backend with a 30 second timeout
            response = requests.post(BACKEND_URL, json=payload, timeout=30)
            return response.json()
        except requests.exceptions.RequestException:
            return {
                "success": False,
                "message": "Unable to connect to backend.",
                "data": {}
            }
    else:
        # Fallback to urllib if requests is not available
        try:
            data = json.dumps(payload).encode("utf-8")
            req = urllib.request.Request(
                BACKEND_URL, data=data, headers={"Content-Type": "application/json"}, method="POST"
            )
            with urllib.request.urlopen(req, timeout=30) as resp:
                resp_data = resp.read().decode("utf-8")
                return json.loads(resp_data)
        except Exception:
            return {
                "success": False,
                "message": "Unable to connect to backend.",
                "data": {}
            }