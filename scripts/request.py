"""Tes the api by making a call."""

import requests
from sudoku.core.extract_square import csv_to_image
import os

os.chdir('..')


def numeric_image():
    """Post a numeric image."""
    image = csv_to_image(1)
    r = requests.post('http://localhost:5000/numeric_image',
                      data={'numeric_image': image})

    print(r)


if __name__ == '__main__':
    pass
