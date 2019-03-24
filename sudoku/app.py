"""Web application main file."""

from flask import Flask, render_template, request
import os

UPLOAD_FOLDER = '/upload'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd() + UPLOAD_FOLDER


@app.route('/')
def home():
    """Home page."""
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_image():
    """Upload image route."""
    file = request.files['image']
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return render_template('index.html')


def process_image():
    """Given an image process it."""
