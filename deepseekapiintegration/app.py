import os
import requests
import streamlit as st
from logger import log_error

API_URL = "https://api.deepseek.com/v1/chat/completions"

# ---------------- CSS STYLES ----------------
st.markdown("""
<style>
/* Main background */
.stApp {
    background-color: #f5f7fb;
    font-family: "Segoe UI", sans-serif;
}

/* Centered container */
.main > div {
    max-width: 900px;
    padding-top: 2rem;
}

/* Header */
.app-title {
    text-align: center;
    font-size: 2.2rem;
    font-weight: 700;
    margin-bottom: 0.3rem;
}

.app-subtitle {
    text-align: center;
    color: #6b7280;
    margin-bottom: 2rem;
}

/* Chat bubbles */
.chat-user {
    background-color: #2563eb;
    color: white;
    padding: 12px 16px;
    border-radius: 16px;
    margin-bottom: 8px;
    width: fit-content;
    max-width: 80%;
    margin-left: auto;
}

.chat-assistant {
    background-color: white;
    color: #111827;
    padding: 12px 16px;
    border-radius: 16px;
    margin-bottom: 8px;
    width: fit-content;
    max-width: 80%;
    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
}

/* Input box */
textarea {
    border-radius: 12px !important;
}

/* Footer hint */
.footer-text {
    text-align: center;
    color: #9ca3af;
    font-size: 0.85rem;
    margin-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

# ---------------- BACKEND LOGIC ----------------
def fallback_response():
    return (
        "• DeepSeek API authentication failed\n"
        "• The error was logged successfully\n"
        "• This is a fallback response\n"
        "• The application continues to work"
    )

def get_assistant_reply(user_message: str) -> str:
    api_key = os.getenv("DEEPSEEK_API_KEY")

    headers = {
        "Authorization": f"Bearer {api_key}" if api_key else "",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant. "
                    "Format responses using bullet points or numbered lists "
                    "when appropriate."
                )
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    }

    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=30
        )

        if response.status_code != 200:
            log_error(response.text)
            return fallback_response()

        data = response.json()
        return data["choices"][0]["message"]["content"]

    except Exception as e:
        log_error(str(e))
        return fallback_response()

# ---------------- STREAMLIT UI ----------------
st.markdown('<div class="app-title">💬 DeepSeek Chat Assistant</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="app-subtitle">A professional AI chat interface with error handling and logging</div>',
    unsafe_allow_html=True
)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="chat-user">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-assistant">{msg["content"]}</div>', unsafe_allow_html=True)

# Chat input
user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    reply = get_assistant_reply(user_input)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()

st.markdown(
    '<div class="footer-text">Built for ML Internship Task • Streamlit + DeepSeek API</div>',
    unsafe_allow_html=True
)
