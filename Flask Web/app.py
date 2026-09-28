from flask import Flask, render_template
import os

app = Flask(__name__)

PYTHON_FILE = "easy.py"
SUPPORT_FILE = "nth.py"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPT_PATH = os.path.join(BASE_DIR, PYTHON_FILE)
SUPPORT_PATH = os.path.join(BASE_DIR, SUPPORT_FILE)

def read_file(path, fallback):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return fallback


@app.route("/")
def index():
    source_code = read_file(SCRIPT_PATH, "# Main Python file not found on server")
    support_code = read_file(SUPPORT_PATH, "# Support file not found on server")

    return render_template(
        "index.html",
        python_file=PYTHON_FILE,
        source_code=source_code,
        support_file=SUPPORT_FILE,
        support_code=support_code
    )
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
