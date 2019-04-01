"""
Script to solve a sudoku puzzle.

The algorithm will work by first finding low hanging fruit
and if no obvious moves available use a standard backtracking algorithm

The sudoku board will be 9x9 list inside a list.

First index is row and second index is column
0 represents empty square
"""


class GameOfSudoku(object):
    """
    Class which takes a unsolved puzzle and solves it.

    This class contains a check functions is_valid & check_list.
    Can find elements of the board like get_neg.
    Also there are three functions which add elements to the board.
    The final function contains a backtracking recursive function
    which also can return the faliure conditon if reached.
    """

    # Parse the inputted board to the game
    def __init__(self, game):
        """__init__ takes a 2d list which becomes the board."""
        self.old = [inner_list[:] for inner_list in game]
        self.wrong = []
        self.track = 0
        self.result = self.back_track([inner_list[:] for inner_list in game])

    # Check validity
    def is_valid(self, board):
        """
        Check if the initial board makes is valid.

        The function takes the class GameOfSudoku and checks the board.
        Normal errors are duplicated entries in the same row, box or columns.
        """
        # Valid key
        validity = 0

        # Check each row
        for row in board:
            if not check_list(row):
                validity = validity + 1

        # Check each column
        for col in range(0, 9):
            flat_col = []
            for row in board:
                flat_col.append(row[col])
            if not check_list(flat_col):
                validity = validity + 1

        # Check each 9x9 square
        for col_start in [0, 3, 6]:
            for row_start in [0, 3, 6]:
                flat_square = []
                for col in range(col_start, col_start+3):
                    for row in range(row_start, row_start+3):
                        flat_square.append(board[row][col])
                if not check_list(flat_square):
                    validity = validity + 1

        # output
        return validity == 0

    # Possible moves for each cell
    def available_entries(self, row_loc, col_loc, board):
        """
        Obtain possible moves for a individual square.

        Works by checking what is not currently in the row.
        What is not currently in the column and lastly the square.
        """
        # CheckRow
        from_row = []
        for value in range(1, 10):
            if value not in board[row_loc]:
                from_row.append(value)

        # Check column
        from_col = []
        flat_col = []
        for row in board:
            flat_col.append(row[col_loc])
        for value in range(1, 10):
            if value not in flat_col:
                from_col.append(value)

        # Check square
        from_square = []

        # Which row does the square start
        if row_loc/3 < 1:
            start_row = 0
        elif row_loc/3 < 2:
            start_row = 3
        else:
            start_row = 6

        # Whcih column does the square start
        if col_loc/3 < 1:
            start_col = 0
        elif col_loc/3 < 2:
            start_col = 3
        else:
            start_col = 6

        # Add the values to the square
        flat_square = []
        for col in range(start_col, start_col+3):
            for row in range(start_row, start_row+3):
                flat_square.append(board[row][col])
        for value in range(1, 10):
            if value not in flat_square:
                from_square.append(value)

        # Check each value is in the all 3 lists
        output = []
        for value in from_row:
            if (value in from_col) & (value in from_square):
                output.append(value)

        return output

    # Find possible valid moves
    def get_moves(self, board):
        """

        Take the board and return the possible moves for each box in the 9x9.

        The function creates a negative of the board with every possible move.

        """
        available = []
        # Iterate through grid
        for row in range(0, 9):
            row_list = []
            for col in range(0, 9):
                if board[row][col] == 0:
                    row_list.append(self.available_entries(row, col, board))
                else:
                    row_list.append([])
            available.append(row_list)
        return available

    # Easiest moves
    def add_easy(self, neg, input_board):
        """Add easy one option only moves."""
        for row in range(0, 9):
            for col in range(0, 9):
                if len(neg[row][col]) == 1:
                    input_board[row][col] = neg[row][col][0]
        return input_board

    # Easy rows
    def easy_rows(self, neg, input_board):
        """If one value can only land in one position of a row then add."""
        for row in range(0, 9):
            for val in range(1, 10):
                if val not in input_board[row]:
                    possible = []
                    for col in range(0, 9):
                        if val in neg[row][col]:
                            possible.append(col)
                    if len(possible) == 1:
                        input_board[row][possible[0]] = val
        return input_board

    # Easy columns
    def easy_columns(self, neg, input_board):
        """If one value can only land in one position of a column then add."""
        for col in range(0, 9):
            flat_col = []
            for row in input_board:
                flat_col.append(row[col])
            for val in range(1, 10):
                if val not in flat_col:
                    possible = []
                    for sec_row in range(0, 9):
                        if val in neg[sec_row][col]:
                            possible.append(sec_row)
                    if len(possible) == 1:
                        input_board[possible[0]][col] = val
        return input_board

    # Check if there is only one possible value in the square
    def easy_square(self, neg, input_board):
        """If one value can only land in one position of a square then add."""
        for col_start in [0, 3, 6]:
            for row_start in [0, 3, 6]:
                flat_square = []
                for col in range(col_start, col_start+3):
                    for row in range(row_start, row_start+3):
                        flat_square.append(input_board[row][col])
                for val in range(1, 10):
                    if val not in flat_square:
                        possible = []
                        for col in range(col_start, col_start+3):
                            for row in range(row_start, row_start+3):
                                if val in neg[row][col]:
                                    possible.append((row, col))
                        if len(possible) == 1:
                            input_board[possible[0][0]][possible[0][1]] = val
        return input_board

    def back_track(self, board):
        """
        Back track recursive function.

        This function takes a copy of a board, attempts to find a basic
        solution, calls the complex functions and finally after exhausting
        all other options performs a backtracking algorithm.
        """
        aim = zero_check(board)

        if aim == 0:
            self.complete = board
            return True

        neg = self.get_moves(board)

        # Do the moves
        board = self.add_easy(neg, [inner_list[:] for inner_list in board])
        board = self.easy_rows(neg, [inner_list[:] for inner_list in board])
        board = self.easy_columns(neg, [inner_list[:] for inner_list in board])
        board = self.easy_square(neg, [inner_list[:] for inner_list in board])

        # Check for new stuff
        if zero_check(board) != aim:
            return self.back_track(board)

        new_vals = []
        for row in range(0, 9):
            for col in range(0, 9):
                if neg[row][col]:
                    new_vals.append([row, col])

        if new_vals:
            self.wrong.append(board)
            return False

        for val in new_vals:
            for attempt in neg[val[0]][val[1]]:
                board[val[0]][val[1]] = attempt
                if self.back_track(board):
                    self.complete = board
                    return True
                else:
                    board[val[0]][val[1]] = 0
        return False


def check_list(entity):
    """Check if a number is repeated in a list of length 9."""
    for key in range(0, 9):
        for compare in range(key+1, 9):
            if (entity[key] == entity[compare]) & (entity[key] != 0):
                return False
    return True


def zero_check(grid):
    """Take a 2d grid and calculates number of 0 entries."""
    zeros = 0
    for row in grid:
        for element in row:
            if element == 0:
                zeros += 1
    return zeros
