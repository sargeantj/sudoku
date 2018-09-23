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


def get_model():
    """Return the model used to predict a number."""
    # Sequential Model
    model = kr.models.Sequential()

    # Layers
    model.add(kr.layers.Conv2D(32, input_shape=(33, 33, 1),
                               kernel_size=(5, 5), activation='relu',
                               padding='same'))
    model.add(kr.layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2),
                                  padding='same'))
    model.add(kr.layers.Conv2D(64, kernel_size=(5, 5), activation='relu',
                               padding='same'))
    model.add(kr.layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2),
                                  padding='same'))
    model.add(kr.layers.Dense(10, activation='relu'))

    # Compile
    model.compile(optimizer='adam', loss='categorical_crossentropy')

    # Return the model
    return model



import extract_square as es
data = es.csv_to_image(1)

y = [8, 0, 0, 4, 0, 0, 6, 0, 1, 2, 0, 0, 6, 0, 5, 8, 4, 0, 0, 0, 0, 0, 0,
     0, 0, 5, 0, 0, 0, 6, 5, 4, 0, 0, 0, 8, 5, 0, 0, 0, 0, 0, 0, 1, 0, 0,
     0, 1, 8, 2, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 9, 0, 6, 0, 0, 1, 0, 8,
     4, 7, 0, 3, 0, 0, 9, 0, 0, 1, 0, 5]

oney = one_hot_y(y)

x = scale_image(data)

q = np.array(x)

my_y = np.array(np.array(oney))

model = get_model()

model.fit(x=q, y=my_y, epochs=10, batch_size=81)
