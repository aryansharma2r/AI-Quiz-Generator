# prompt.py
# This file is responsible for building the prompt string
# that will be sent to the AI model (Gemini/OpenAI) later.
# It does NOT call any AI API - it only creates the prompt text.

def build_quiz_prompt(topic: str, difficulty: str, question_count: int, question_type: str) -> str:
    """
    Builds a formatted prompt string instructing the AI to generate a quiz.

    Parameters:
        topic (str): The topic for the quiz.
        difficulty (str): Difficulty level of the quiz.
        question_count (int): Number of questions to generate.
        question_type (str): Type of questions (e.g. MCQ, True/False).

    Returns:
        str: A complete prompt string ready to be sent to the AI model.
    """

    # Multi-line prompt string with clear instructions for the AI.
    # This ensures the AI returns clean, structured JSON output only.
    prompt = f"""
You are a quiz generator AI. Generate a quiz based on the following details:

Topic: {topic}
Difficulty: {difficulty}
Number of Questions: {question_count}
Question Type: {question_type}

Instructions:
1. Generate questions ONLY on the given topic.
2. Follow the requested difficulty level strictly.
3. Generate exactly {question_count} questions.
4. Use the requested question type: {question_type}.
5. Return ONLY valid JSON. Do NOT include any explanations.
6. Do NOT include markdown formatting (no ```json or ```).
7. Do NOT include any extra text before or after the JSON.

Return the JSON in this exact structure:
{{
    "questions": [
        {{
            "question": "string",
            "options": ["string", "string", "string", "string"],
            "correct_answer": "string"
        }}
    ]
}}
"""

    # Return the final prompt string
    return prompt
