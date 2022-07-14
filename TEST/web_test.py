import sys
from flask import Flask, render_template, send_from_directory
from config import directory_to_image_folder
app = Flask(__name__)



@app.route('/')
def download_file(filename):
    return send_from_directory(directory_to_image_folder, filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
