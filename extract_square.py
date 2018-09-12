"""

Read in images and binarize to reduce down into a square.

"""

# Packages
import cv2
import numpy as np
import pandas as pd

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
    pts_from = np.float32(corners)
    pts_to = np.float32([[0, 0], [0, 299], [299, 299], [299, 0]])

    rotation = cv2.getPerspectiveTransform(pts_from, pts_to)

    dst = cv2.warpPerspective(image, rotation, (300, 300))
    return dst


def extract_square(image_number=1):
    """Given a number of the image file return a cropped sudoku."""
    image_string = '/home/james/Documents/Code/sudoku/python-sudoku/img/'
    image_string += str(image_number) + '.jpg'

    binary = read_binary(image_string)
    threshold = get_threshold(binary)
    square = get_square_coordinates(threshold)
    game = extract_sudoku(square, threshold)

    return game


def image_to_csv(image_number):
    """
    Write to file the data from an image.

    This is a reverse of the function image to csv.
    """
    game = extract_square(image_number)

    x_max = [33, 66, 99, 132, 166, 199, 232, 266, 299]
    x_min = [0, 33, 66, 99, 133, 166, 199, 233, 266]
    y_max = [33, 66, 99, 132, 166, 199, 232, 266, 299]
    y_min = [0, 33, 66, 99, 133, 166, 199, 233, 266]
    pictures = []
    for x_coord in range(9):
        for y_coord in range(9):
            current = []
            for horiz in range(x_min[x_coord], x_max[x_coord]):
                row = []
                for verti in range(y_min[y_coord], y_max[y_coord]):
                    row.append(game[horiz][verti])
                current.append(row)
            pictures.append(current)

    result = []
    for picutre in pictures:
        picture_row = []
        for line in picutre:
            picture_row += line
        result.append(picture_row)

    picture_frame = pd.DataFrame(result)
    picture_frame.to_csv("/home/james/Documents/Code/sudoku/"
                         + 'python-sudoku/training/image_' + str(image_number)
                         + '.csv',
                         header=False, index=False)


def csv_to_image(image_number):
    """
    Given a csv file transform back to a lists of lists of list for.

    This is a reverse of the function image_to_csv
    """
    image = pd.read_csv("/home/james/Documents/Code/sudoku/"
                        + 'python-sudoku/training/image_' + str(image_number)
                        + '.csv', header=None)
    result = []
    for row in range(image.shape[0]):
        raw = list(image.loc[row])
        singular_image = []
        subset = []
        for index, value in enumerate(raw):
            if (index % 33 == 0) & (index != 0):
                singular_image.append(subset)
                subset = []
            subset.append(value)
            if index == 1088:
                singular_image.append(subset)
        result.append(singular_image)
    return result
