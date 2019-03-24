"""Tes the api by making a call."""

import requests
from extract_square import csv_to_image


def numeric_image():
    """Post a numeric image."""
    image = csv_to_image(1)
    r = requests.post('http://localhost:5000/numeric_image',
                      data={'numeric_image': image})

    print(r)


if __name__ == '__main__':
    pass
