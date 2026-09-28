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

@app.route("/debug")
def debug():
    import subprocess
    files = {f: os.path.getsize(os.path.join(BASE_DIR, f)) for f in os.listdir(BASE_DIR)}
    return {
        "base_dir": BASE_DIR,
        "files_and_sizes": files,
        "easy_py_preview": read_file(SCRIPT_PATH, "NOT FOUND")[:200],
    }
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
