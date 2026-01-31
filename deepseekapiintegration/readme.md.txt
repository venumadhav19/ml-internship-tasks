DeepSeek Chat Assistant
Overview

This project is a web-based AI chat application developed using Python and Streamlit.

It demonstrates API integration, structured response handling, error logging, and graceful fallback mechanisms.

The application was built as part of an ML Internship task to showcase practical software engineering skills.

Key Features

Web-based chat interface built with Streamlit

Multi-turn conversational support using session state

Integration logic for the DeepSeek REST API

Structured and formatted responses (bullet points or numbered lists)

Robust error handling for API and runtime failures

Automatic error logging to a file

Graceful fallback responses when API authentication fails

Clean and professional user interface with custom CSS styling

Technologies Used

Python 3

Streamlit

Requests library

DeepSeek REST API

Project Structure
deepseekapiintegration/
├── app.py        # Main Streamlit application
├── logger.py     # Utility for logging errors
├── error.log     # Auto-generated error log file
└── README.md     # Project documentation

How to Run the Application
Step 1: (Optional) Create and activate a virtual environment
python -m venv venv


Activate on Windows:

venv\Scripts\activate

Step 2: Install required dependencies
pip install streamlit requests

Step 3: Set the DeepSeek API key as an environment variable
setx DEEPSEEK_API_KEY "YOUR_DEEPSEEK_API_KEY"


Restart the terminal after setting the environment variable.

The API key is not hardcoded anywhere in the source code.

Step 4: Run the application
streamlit run app.py


Open the browser at: http://localhost:8501

API Authentication and Fallback Handling

DeepSeek API integration is implemented using the official REST endpoint.

Free-tier API keys may return authentication errors due to platform restrictions.

The application handles such cases by:

Catching API errors safely

Logging errors to error.log

Displaying a fallback response to the user

Ensuring the application does not crash

This approach reflects real-world production practices where external APIs may fail or be restricted.

Error Handling and Logging

All API and runtime errors are captured using exception handling.

Errors are logged with timestamps in the error.log file.

Logging is implemented in a separate utility module for better code organization.

Learning Outcomes

Practical experience with REST API integration

Secure handling of API keys using environment variables

Streamlit-based web application development

Graceful handling of third-party API failures

Writing clean, modular, and maintainable Python code

Submission Notes

Virtual environment and cache folders are excluded from submission

No API keys or sensitive data are included

The project is structured, documented, and ready for evaluation

Author

Venu Madhav
ML Internship Candidate