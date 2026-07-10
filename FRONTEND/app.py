# app.py
# This is the Streamlit frontend for the AI Quiz Generator.
# It collects user input, validates it, and integrates with the backend
# using the generate_quiz() function from utils.py.

import importlib

try:
    st = importlib.import_module("streamlit")
except ModuleNotFoundError as e:
    raise ModuleNotFoundError(
        "Streamlit is required to run this app. Install it with 'pip install streamlit'."
    ) from e

from utils import generate_quiz

# Set the page configuration (title, icon, layout)
st.set_page_config(
    page_title="AI Quiz Generator",
    page_icon="📝",
    layout="centered"
)

# Display the main title of the app
st.title("AI Quiz Generator")

# Display a short description below the title
st.write("Generate AI-powered quizzes using Gemini AI.")

# --- Input Fields ---

# Text input for the quiz topic
topic = st.text_input("Topic")

# Selectbox for difficulty level
difficulty = st.selectbox(
    "Difficulty",
    options=["Easy", "Medium", "Hard"]
)

# Number input for number of questions (min=1, max=20, default=5)
question_count = st.number_input(
    "Question Count",
    min_value=1,
    max_value=20,
    value=5
)

# Selectbox for question type
question_type = st.selectbox(
    "Question Type",
    options=["MCQ", "True/False"]
)

# --- Generate Button ---

# When the button is clicked, validate input and call the backend
if st.button("Generate Quiz"):

    # Validate that the topic field is not empty (also handles whitespace-only input)
    if topic.strip() == "":
        st.warning("Please enter a topic.")

    else:
        # Show a spinner while waiting for the backend response
        with st.spinner("Generating quiz..."):
            response = generate_quiz(topic, difficulty, question_count, question_type)

        # If the backend request was successful
        if response.get("success") is True:

            # Show success message
            st.success(response.get("message"))

            # Display heading for the generated quiz
            st.subheader("Generated Quiz")

            # Safely read the questions list, defaulting to an empty list if missing
            questions = response.get("data", {}).get("questions", [])

            # If no questions were returned, show a warning instead of an empty screen
            if not questions:
                st.warning("No quiz questions were returned.")
            else:
                # Loop through each question and display it
                for index, q in enumerate(questions, start=1):
                    st.divider()
                    st.write(f"**Question {index}**")
                    st.write(q.get("question", ""))

                    # Display all options
                    st.write("**Options**")
                    for option in q.get("options", []):
                        st.write(f"• {option}")

                    # Display the correct answer
                    st.write("**Correct Answer**")
                    st.success(q.get("correct_answer", ""))

                st.divider()

        # If the backend request failed
        else:
            st.error(response.get("message", "Something went wrong."))