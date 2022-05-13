import time


def main():

    # This is the example board for this algorhythm
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    # This will solve the board, measure the time it takes to do so,
    # print the board to the screen with the time taken to execute.
    startTime = time.time()
    fillBlankSpaces(board, 0, 0)
    completionTime = "{:.5f}".format(time.time() - startTime)
    print(f"Completed in {completionTime} seconds.")
    printBoard(board)


def fillBlankSpaces(board, row, col):
    currentRow = row
    currentCol = col

    # Check if we have got to the last column and start a new row if so.
    if currentCol == len(board[currentRow]):
        currentRow += 1
        currentCol = 0

        # If the row is eqaul to the length of the board then we have filled in all
        # all spaces and can return true.
        if currentRow == len(board):
            return True

    # If a digit is 0 then we need to explore what the value could be via back track.       
    if board[currentRow][currentCol] == 0:
        return tryDigits(board, currentRow, currentCol)

    # If the value is already filled in then move to the next square.
    return fillBlankSpaces(board, currentRow, currentCol + 1)


def tryDigits(board, row, col):
    # Try every value between 1 and 10.
    for digit in range(1, 10):

        # Check if the digit is a valid placement (not necessarily correct).
        if checkDigitIsValid(board, row, col, digit):

            # If valid then place the digit and move onto the next square
            board[row][col] = digit
            if fillBlankSpaces(board, row, col + 1):
                return True

    # If no valid digit can be placed then start to back track and find
    # where we made a mistake.
    board[row][col] = 0
    return False


def checkDigitIsValid(board, row, col, digit):

    # Check if the digit isn't in the same row or column
    rowValid = digit not in board[row]
    colValid = digit not in map(lambda r: r[col], board)
    if not rowValid or not colValid:
        return False


    # Find the start of the subgrid we need to check.
    # It will either be 0, 3 or 6 and then we have the top left corener of
    # the subgrid and can start to iterate through.
    rowStart = (row // 3) * 3
    colStart = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            rowIdx = rowStart + i
            colIdx = colStart + j

            # If we find the digit in the subgrid then the placement is invalid.
            # Other wise it is valid.
            if board[rowIdx][colIdx] == digit:
                return False
    return True


def printBoard(board):

    # This functions reformats the board to make it easier to read in the console.
    print("- - - - - - - - - - - - -")
    for i in range(len(board)):
        if i % 3 ==0 and i != 0:
            print("- - - - - - - - - - - - -")
        for j in range(len(board[0]) + 1):
            if j % 3 == 0 and j != 9:
                print("| ", end="")
            if j == 9:
                print("|", end="\n")
            else:
                print(str(board[i][j]) + " ", end="")
    print("- - - - - - - - - - - - -")


if __name__ == "__main__":
    main()