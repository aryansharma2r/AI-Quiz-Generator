# helpers.py
# This file contains simple, reusable helper functions
# for general text processing. It is not tied to any
# specific feature like quizzes, AI, or API logic.


def clean_text(text: str) -> str:
    """
    Removes leading and trailing whitespace from a string.

    Parameters:
        text (str): The input string to clean.

    Returns:
        str: The cleaned string with no leading/trailing whitespace.
    """
    # strip() removes whitespace (spaces, tabs, newlines) from both ends
    return text.strip()


def is_empty(text: str) -> bool:
    """
    Checks whether a string is empty or contains only whitespace.

    Parameters:
        text (str): The input string to check.

    Returns:
        bool: True if the string is empty or whitespace-only, False otherwise.
    """
    # After stripping whitespace, if nothing remains, the string is considered empty
    return len(text.strip()) == 0