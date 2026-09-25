from flask import Flask, render_template
import os

app = Flask(__name__)

PYTHON_FILE = "easy.py" 
SUPPORT_FILE = "nth.py"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPT_PATH = os.path.join(BASE_DIR, PYTHON_FILE)
SUPPORT_PATH = os.path.join(BASE_DIR, SUPPORT_FILE)

try:
    with open(SUPPORT_PATH, "r", encoding="utf-8") as file:
        SUPPORT_CODE_CONTENT = file.read()
except FileNotFoundError:
    SUPPORT_CODE_CONTENT = "# Support file not found on server"

@app.route("/")
def index():
    try:
        with open(SCRIPT_PATH, "r", encoding="utf-8") as file:
            source_code = file.read()
    except FileNotFoundError:
        source_code = "# Main Python file not found on server"


    return render_template(
        "index.html",
        easy_py_name=PYTHON_FILE,
        easy={"py": source_code},
        support_file=SUPPORT_FILE,
        support_code=SUPPORT_CODE_CONTENT
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
