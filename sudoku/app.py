"""Web application main file."""

# Packages
from flask import Flask, render_template, request
from core.extract_square import extract_square_from_image, partition
from core.model import Model, scale_image, reverse_one_hot
from core.translation import numbers_to_game
from core.game import GameOfSudoku
import os
import tensorflow as tf
import numpy as np


# Flask config
UPLOAD_FOLDER = '/upload'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd() + UPLOAD_FOLDER

# Load the model into memory
model = Model()
model.load()
# Clear tensorflow
graph = tf.get_default_graph()


@app.route('/')
def home():
    """Home page."""
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_image():
    """Upload image route."""
    file = request.files['image']
    result = process_image(file.read())
    return render_template('result.html', result=result)


def process_image(image):
    """Given an image process it."""
    # Tensorflow
    global graph
    with graph.as_default():
        # Extract the game from the image.
        game_square = extract_square_from_image(image)
        game_images = partition(game_square)

        # Call the model
        scaled_data = scale_image(game_images)
        array = np.array(scaled_data)
        prediction = model.model.predict(array)
        result = reverse_one_hot(prediction)
        raw = numbers_to_game(result)
        Game = GameOfSudoku(raw)
        if Game.result:
            return Game.complete
        else:
            return 'Something went wrong'
