"""Read in images and binarize to reduce down into a square."""


import cv2
from matplotlib import pyplot as plt
import numpy as np


# Choose binary

image_str = 1

img = cv2.imread('/home/james/Documents/Code/sudoku/python-sudoku/img/' + str(image_str) + '.jpg')

# De-colour
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


gray = cv2.GaussianBlur(gray, (5, 5), 0)


# Threshold
# Inverted for findContours
# Binary with 127
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)


# Find edges of sudoku using contours
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

biggest = None
max_area = 0
numba = 0
for count, i in enumerate(contours):
    area = cv2.contourArea(i)
    peri = cv2.arcLength(i, True)
    approx = cv2.approxPolyDP(i, 0.02*peri, True)
    if area > max_area and len(approx) == 4:
        biggest = approx
        max_area = area
        numba = count


plt.figure()
plt.imshow(cv2.drawContours(img, [biggest], -1, (0, 255, 0), 3))
plt.show()


def contour_2_list(contour, image):
    """Use the contours and return as ordered list."""
    output = []
    for pair in contour:
        output.append([pair[0][0], pair[0][1]])

    max = 0
    min = len(image) + len(image[0])
    for index, value in enumerate(corners):
        if sum(value) >= max:
            tr = index
            max = sum(value)
        if sum(value) <= min:
            bl = index
            min = sum(value)

    for index in range(4):
        if index not in [bl, tr]:
            if corners[index][0] > corners[index][1]:
                br = index
            else:
                tl = index

    return [output[bl], output[tl], output[tr], output[br]]


corners = contour_2_list(biggest, img)


ptsFrom = np.float32(corners)
ptsTo = np.float32([[0, 0], [0, 299], [299, 299], [299, 0]])

M = cv2.getPerspectiveTransform(ptsFrom, ptsTo)

dst = cv2.warpPerspective(thresh, M, (300, 300))
