"""Local Flask entry point for the portfolio."""
import json
from pathlib import Path
from flask import Flask, render_template

app = Flask(__name__)
PROJECTS_FILE = Path(__file__).parent / "data" / "projects.json"

@app.route("/")
def home():
    with PROJECTS_FILE.open(encoding="utf-8") as file:
        projects = json.load(file)
    return render_template("index.html", projects=projects)

if __name__ == "__main__":
    app.run(debug=True)
