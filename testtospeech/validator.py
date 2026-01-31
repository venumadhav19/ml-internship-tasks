import re

def validate_text(text: str) -> str:
    if not text or text.strip() == "":
        raise ValueError("Text input cannot be empty")

    # Remove unsupported special characters
    cleaned_text = re.sub(r"[^a-zA-Z0-9.,!? ]+", "", text)

    return cleaned_text.strip()
