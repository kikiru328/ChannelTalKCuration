import sys
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", image_file='식단표.png')

if __name__ == "__main__":
    app.run(debug=True)
