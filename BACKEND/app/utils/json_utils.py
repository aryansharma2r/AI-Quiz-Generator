# json_utils.py
# This file contains simple, reusable JSON utility functions
# for converting between Python dictionaries and JSON strings.
# It is not tied to any specific feature like quizzes or APIs.

import json


def dict_to_json(data: dict) -> str:
    """
    Converts a Python dictionary into a formatted JSON string.

    Parameters:
        data (dict): The dictionary to convert.

    Returns:
        str: A formatted JSON string with an indent of 4 spaces.
    """
    # json.dumps() converts a dict into a JSON string
    # indent=4 makes the output nicely formatted and readable
    return json.dumps(data, indent=4)


def json_to_dict(json_text: str) -> dict:
    """
    Converts a JSON string into a Python dictionary.

    Parameters:
        json_text (str): The JSON string to convert.

    Returns:
        dict: The resulting Python dictionary.
    """
    # json.loads() parses a JSON string into a Python dictionary
    return json.loads(json_text)