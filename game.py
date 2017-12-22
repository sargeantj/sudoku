# Script to solve a sudoku puzzle

# The algorithm will work by first finding low hanging fruit
# and if no obvious moves available use a standard backtracking algorithm


# The sudoku board will be 9x9 list inside list.
# First index is row and second index is column

# 0 represents empty square



test = [[8,0,0,4,0,0,6,0,1],
        [2,0,0,6,0,5,8,4,0],
        [0,0,0,0,0,0,0,5,0],
        [0,0,6,5,4,0,0,0,8],
        [5,0,0,0,0,0,0,1,0],
        [0,0,1,8,2,0,0,0,3],
        [0,0,0,0,0,0,0,9,0],
        [6,0,0,1,0,8,4,7,0],
        [3,0,0,9,0,0,1,0,5]]


class gameOfSudoku:

    def __init__(self, game):
        self.board = game

    # Check validity
    def isValid(self):

        # Valid key
        validity = 0

        # Check each row
        for row in self.board:
            if checkList(row) == False:
                validity = validity + 1

        # Check each column
        for col in range(0, 9):
            flatCol = []
            for row in self.board:
                flatCol.append(row[col])
            if checkList(flatCol) == False:
                validity = validity + 1


        # Check each 9x9 square
        for colStart in [0, 3, 6]:
            for rowStart in [0, 3, 6]:
                flatSquare = []
                for col in range(colStart,colStart+3):
                    for row in range(rowStart, rowStart+3):
                        flatSquare.append(self.board[row][col])
                if checkList(flatSquare) == False:
                    validity = validity + 1

        # output
        return(validity == 0)



    # Check if any value in a list is repeated
    def checkList(entity):
        for key in range(0, 9):
            for compare in range(key+1, 9):
                if (entity[key] == entity[compare]) & (entity[key] != 0):
                    return(False)
        return(True)



    # Possible moves for each cell
    def availableEntries(self, rowLoc, colLoc):

        # CheckRow
        fromRow = []
        for value in range(1, 10):
            if (value in self.board[rowLoc]) == False:
                fromRow.append(value)

        # Check column
        fromCol = []
        flatCol = []
        for row in self.board:
            flatCol.append(row[colLoc])
        for value in range(1, 10):
            if (value in flatCol) == False:
                fromCol.append(value)

        # Check square
        fromSquare = []

        if rowLoc/3 < 1:
            startRow = 0
        elif rowLoc/3 < 2:
            startRow = 3
        else:
            startRow = 6

        if colLoc/3 < 1:
            startCol = 0
        elif colLoc/3 < 2:
            startCol = 3
        else:
            startCol = 6

        flatSquare = []
        for col in range(startCol,startCol+3):
            for row in range(startRow, startRow+3):
                flatSquare.append(self.board[row][col])
        for value in range(1, 10):
            if (value in flatSquare) == False:
                fromSquare.append(value)

        # Check each value is in the all 3 lists
        output = []
        for value in fromRow:
            if (value in fromCol) & (value in fromSquare):
                output.append(value)

        return(output)



    # Find possible valid moves
    def getMoves(self):

        available = []
        # Iterate through grid
        for row in range(0, 9):
            rowList = []
            for col in range(0, 9):
                if self.board[row][col] == 0:
                    rowList.append(self.availableEntries(row, col))
                else:
                    rowList.append([])
            available.append(rowList)
        return(available)



    # Easiest moves
    def addEasy(self, neg):
        for row in range(0, 9):
            for col in range(0, 9):
                if len(neg[row][col]) == 1:
                    self.board[row][col] = neg[row][col][0]




    # Easy rows
    def easyRows(self, neg):
        for row in range(0, 9):
            for val in range(1, 10):
                if (val in self.board[row]) == False:
                    possible = []
                    for col in range(0, 9):
                        if val in neg[row][col]:
                            possible.append(col)
                    if len(possible) == 1:
                        self.board[row][possible[0]] = val



# Easy columns
    def easyColumns(self, neg):
        for col in range(0, 9):
            flatCol = []
            for row in self.board:
                flatCol.append(row[col])
            for val in range(1, 10):
                if (val in flatCol) == False:
                    possible = []
                    for secRow in range(0, 9):
                        if val in neg[secRow][col]:
                            possible.append(secRow)
                    if len(possible) == 1:
                        self.board[possible[0]][col] = val



# Check if there is only one possible value in the square
    def easySquare(self, neg):
        for colStart in [0, 3, 6]:
            for rowStart in [0, 3, 6]:
                flatSquare = []
                for col in range(colStart,colStart+3):
                    for row in range(rowStart, rowStart+3):
                        flatSquare.append(self.board[row][col])
                for val in range(1, 10):
                    if (val in flatSquare) == False:
                        possible = []
                        for col in range(colStart,colStart+3):
                            for row in range(rowStart, rowStart+3):
                                if val in neg[row][col]:
                                    possible.append((row, col))
                        if len(possible) == 1:
                            self.board[possible[0][0]][possible[0][1]] = val


    def zeroCheck(grid):

        zeros = 0
        for row in grid:
            for element in row:
                if element == 0:
                    zeros = zeros +1

        return(zeros)




    def backTrack(self):

        aim = zeroCheck(self.board)

        if aim == 0:
            return(True)

        neg = self.getMoves()

    # Do the moves
        self.addEasy(neg)
        self.easyRows(neg)
        self.easyColumns(neg)
        self.easySquare(neg)

    # Check for new stuff
        if zeroCheck(self.board) != aim:
            return(self.backTrack())




        newVals = []
        for row in range(0, 9):
            for col in range(0, 9):
                if len(neg[row][col]) > 0:
                    newVals.append([row, col])


        if len(newVals) == 0:
            return(False)
        else:
            for val in newVals:
                newCop = gameOfSudoku(self.board)
                newCop.board[val[0]][val[1]] = neg[val[0]][val[1]]
                if newCop.backTrack():
                    return(True)
            return(False)






def checkList(entity):
    for key in range(0, 9):
        for compare in range(key+1, 9):
            if (entity[key] == entity[compare]) & (entity[key] != 0):
                return(False)
    return(True)


def zeroCheck(grid):

    zeros = 0
    for row in grid:
        for element in row:
            if element == 0:
                zeros = zeros +1

    return(zeros)
