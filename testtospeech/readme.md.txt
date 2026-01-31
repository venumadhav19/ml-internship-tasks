# Text to Speech Converter

## Overview
- This project is a web-based Text to Speech (TTS) application developed using Python and Streamlit.
- It allows users to convert written text into spoken audio using a simple and interactive interface.
- The application was built as part of an ML Internship task to demonstrate frontend integration, validation, and basic AI functionality.

## Key Features
- Web-based user interface built with Streamlit
- Text input area for user-provided content
- Language and voice selection options (accents)
- Adjustable speech speed and volume controls
- Audio playback within the browser
- Input validation to prevent empty or invalid text
- Modular code structure for better maintainability
- Unit tests for validation logic

## Technologies Used
- Python 3
- Streamlit
- gTTS (Google Text-to-Speech)
- Pytest (for unit testing)

## Project Structure
testtospeech/
├── app.py # Main Streamlit application
├── validator.py # Input validation logic
├── test_validator.py # Unit tests for validation
├── output.mp3 # Generated audio file (runtime)
└── README.md # Project documentation
Activate on Windows:

venv\Scripts\activate

Step 2: Install required dependencies
pip install streamlit gtts pytest

Step 3: Run the application
streamlit run app.py


Open the browser at:

http://localhost:8501

Input Validation

The application validates user input before generating speech.

Empty text input is not allowed.

Invalid characters are cleaned before processing.

Validation logic is isolated in a separate module for clarity and testability.

Unit Testing

Unit tests are written using Pytest.

Tests ensure validation behaves correctly for:

Empty input

Special characters

Tests can be executed using:

pytest

Learning Outcomes

Building interactive web applications using Streamlit

Integrating text-to-speech functionality

Writing modular and testable Python code

Implementing input validation and unit testing

Managing application structure for real-world projects

Submission Notes

Virtual environment and cache folders are excluded

Generated audio files are runtime artifacts

The project is clean, tested, and ready for evaluation

Author

Venu Madhav
ML Internship Candidate
