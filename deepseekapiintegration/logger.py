import datetime

def log_error(message: str):
    with open("error.log", "a") as f:
        timestamp = datetime.datetime.now().isoformat()
        f.write(f"[{timestamp}] {message}\n")
