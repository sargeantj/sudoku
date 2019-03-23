"""Rest API page for model."""

from flask import Flask


app = Flask(__name__)


@app.route("/")
def model():
    return 'sdasadsa'
