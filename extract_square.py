"""Read in images and binarize to reduce down into a square."""


import cv2
import numpy as np


def read_binary(input_string):
    """Read and binarize and image."""
    img = cv2.imread(input_string)

    # De-colour
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    return gray


def get_threshold(image):
    """Threshold inverted for findContours using Binary with 127."""
    ret, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

    return thresh


def get_square_coordinates(image):
    """Find edges of sudoku using contours"""
    im2, contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    biggest = None
    max_area = 0
    for i in contours:
        area = cv2.contourArea(i)
        peri = cv2.arcLength(i, True)
        approx = cv2.approxPolyDP(i, 0.02*peri, True)
        if area > max_area and len(approx) == 4:
            biggest = approx
            max_area = area
    return contour_2_list(biggest, image)


def contour_2_list(contour, image):
    """Use the contours and return as ordered list."""
    output = []
    for pair in contour:
        output.append([pair[0][0], pair[0][1]])

    max = 0
    min = len(image) + len(image[0])
    for index, value in enumerate(output):
        if sum(value) >= max:
            tr = index
            max = sum(value)
        if sum(value) <= min:
            bl = index
            min = sum(value)

    for index in range(4):
        if index not in [bl, tr]:
            if output[index][0] > output[index][1]:
                br = index
            else:
                tl = index

    return [output[bl], output[tl], output[tr], output[br]]


def extract_sudoku(corners, image):
    """Using the conrners and image return just the sudoku."""
    ptsFrom = np.float32(corners)
    ptsTo = np.float32([[0, 0], [0, 299], [299, 299], [299, 0]])

    M = cv2.getPerspectiveTransform(ptsFrom, ptsTo)

    dst = cv2.warpPerspective(image, M, (300, 300))
    return dst


def extract_square(image_number=1):
    """Given a number of the image file return a cropped sudoku."""
    myString = '/home/james/Documents/Code/sudoku/python-sudoku/img/' + str(image_number) + '.jpg'

    binary = read_binary(myString)
    threshold = get_threshold(binary)
    square = get_square_coordinates(threshold)
    game = extract_sudoku(square, threshold)

    return game
