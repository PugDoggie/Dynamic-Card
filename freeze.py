# main/freeze.py
import os
from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates",
    static_url_path=""
)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    freezer = Freezer(app)
    freezer.freeze()  # 輸出到 build/