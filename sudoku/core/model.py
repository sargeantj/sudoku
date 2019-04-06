"""Minst model."""

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
        result.append(np.array(current).reshape(33, 33, 1))
    return result


def one_hot_y(list_y):
    """One hot encode the y variable."""
    result = []
    for value in list_y:
        answer = [0]*10
        answer[value] = 1
        result.append(np.float32(answer))
    return result


def reverse_one_hot(array_y):
    """Revers encode a list y."""
    result = []
    for encoded_array in array_y:
        max = 0
        for index, value in enumerate(encoded_array):
            if value > max:
                prediction = index
                max = value
        result.append(prediction)
    return result


class Model(object):
    """Keras MINST model."""

    def __init__(self):
        """Init."""
        pass

    def get_model(self):
        """
        Assign model to a new compiled Model defintion.

        One sudoku has 81 sub images.
        One sample is a 33x33 image.
        Input shape is (33, 33, 1)
        """
        # Sequential Model
        model = kr.models.Sequential()

        # Layers
        model.add(kr.layers.Conv2D(64, input_shape=(33, 33, 1),
                                   kernel_size=(5, 5), activation='relu',
                                   padding='same'))
        model.add(kr.layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2),
                                      padding='same'))
        model.add(kr.layers.Conv2D(32, kernel_size=(5, 5), activation='relu',
                                   padding='same'))
        model.add(kr.layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2),
                                      padding='same'))
        model.add(kr.layers.Flatten())
        model.add(kr.layers.Dense(10, activation='softmax'))

        # Compile
        model.compile(optimizer=kr.optimizers.Adam(lr=0.0001, clipnorm=1),
                      loss='categorical_crossentropy')

        self.model = model

    def save(self, work_directory, folder='model/', name=''):
        """Save the model."""
        self.model.save(work_directory + folder + 'model' + name + '.hdf')

    def load(self, work_directory, folder='/model/', name=''):
        """Load the model."""
        self.model = kr.models.load_model(
            work_directory + folder + 'model' + name + '.hdf')
