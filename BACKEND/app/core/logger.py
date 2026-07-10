# logger.py
# This file sets up a simple, reusable logger for the whole project.
# It prints logs to the console with timestamp, log level, and message.

import logging

# Create a logger instance with a specific name for this project
logger = logging.getLogger("ai_quiz_generator")

# Set the minimum level of messages to handle (INFO and above)
logger.setLevel(logging.INFO)

# Create a console handler to print logs to the terminal
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Define the log message format: timestamp - log level - message
log_format = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Attach the format to the console handler
console_handler.setFormatter(log_format)

# Attach the console handler to the logger
# (avoid adding duplicate handlers if this file is imported multiple times)
if not logger.handlers:
    logger.addHandler(console_handler)