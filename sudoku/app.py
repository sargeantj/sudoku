"""Web application main file."""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    """Home page."""
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_image():
    """Upload image route."""
    file = request.files['image']

    return render_template('index.html')
