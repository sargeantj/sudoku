"""

Transform the square picture of a sudoku to a coded game.

"""

import extract_square as es

game = es.extract_square(3)


x_max = [33, 66, 99, 132, 166, 199, 232, 266, 299]
x_min = [0, 33, 66, 99, 133, 166, 199, 233, 266]
y_max = [33, 66, 99, 132, 166, 199, 232, 266, 299]
y_min = [0, 33, 66, 99, 133, 166, 199, 233, 266]


result = []
for x in range(9):
    for y in range(9):
        current = []
        for horiz in range(x_min[x], x_max[x]):
            row = []
            for verti in range(y_min[y], y_max[y]):
                row.append(game[horiz][verti])
            current.append(row)
        result.append(current)


"""
for x in result:
    plt.figure()
    plt.imshow(x, 'gray')
    plt.show()
"""
res1 = result

res2 = result

test2 = result

label = [8, 0, 0, 4, 0, 0, 6, 0, 1,
         2, 0, 0, 6, 0, 5, 8, 4, 0,
         0, 0, 0, 0, 0, 0, 0, 5, 0,
         0, 0, 6, 5, 4, 0, 0, 0, 8,
         5, 0, 0, 0, 0, 0, 0, 1, 0,
         0, 0, 1, 8, 2, 0, 0, 0, 3,
         0, 0, 0, 0, 0, 0, 0, 9, 0,
         6, 0, 0, 1, 0, 8, 4, 7, 0,
         3, 0, 0, 9, 0, 0, 1, 0, 5]

label2 = [0, 0, 0, 0, 0, 7, 0, 1, 0,
          0, 3, 1, 0, 0, 6, 0, 0, 9,
          0, 7, 0, 0, 1, 4, 5, 0, 0,
          2, 0, 0, 0, 9, 0, 1, 5, 3,
          7, 0, 8, 0, 0, 1, 4, 0, 0,
          0, 0, 0, 4, 0, 0, 0, 0, 0,
          0, 8, 6, 0, 7, 0, 0, 3, 0,
          0, 0, 7, 0, 0, 0, 8, 9, 0,
          3, 0, 0, 0, 2, 5, 0, 0, 0]
