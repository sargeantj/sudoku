"""Tes the api by making a call."""

import requests
from extract_square import csv_to_image

if __name__ == '__main__':
    image = csv_to_image(1)
    r = requests.post('http://localhost:5000/numeric_image',
                      data={'numeric_image': image})

    print(r)
