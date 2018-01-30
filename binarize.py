"""Read in images and binarize to reduce down into a square."""


import cv2
import numpy as np
from matplotlib import pyplot as plt


# Choose binary

image_str = 3

img = cv2.imread('/home/james/Documents/Practice/sudoku/img/' + str(image_str) + '.jpg', 0)

ret, thresh = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

plt.figure()
plt.imshow(thresh, 'gray')

plt.figure()
plt.imshow(img, 'gray')
