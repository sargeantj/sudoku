"""Minst model refactored using keras api instead of tensorflowself."""

# Packages
import numpy as np
from tensorflow import keras as kr


def scale_image(images):
    """Scale the images to [0, 1]."""
    result = []
    for subimage in images:
        current = []
        for row in subimage:
            line = []
            for value in row:
                line.append(np.float32(value/255))
            current.append(line)
        result.append(np.array(current))
    return result


def one_hot_y(list_y):
    """One hot encode the y variable."""
    result = []
    for value in list_y:
        answer = [0]*10
        answer[value] = 1
        result.append(np.float32(answer))
    return result


def get_model():
    """Return the model used to predict a number."""
    model = kr.models.Sequential()
    model.add(kr.layers.Conv2D(32, input_shape=(1, 33, 33), kernel_size=(5, 5),
                               activation='relu', padding='same'))
    model.add(kr.layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2),
                                  padding='same'))
    model.add(kr.layers.Conv2D(64, kernel_size=(5, 5), activation='relu',
                               padding='same'))
    model.add(kr.layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2),
                                  padding='same'))
    model.add()
    return model
