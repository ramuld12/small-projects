import numpy as np
board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]
def valid(x, y, n):
    '''
    Check if a given position in the sudoku is valid for the given number 'n'
    :param x: row
    :param y: column
    :param n: number trying to be placed
    :return: true if the chosen spot is valid for number n. False otherwise
    '''
    global board

    # Check row
    for i in range(0, 9):
        if board[x][i] == n:
            return False

    # Check row
    for i in range(0, 9):
        if board[i][y] == n:
            return False

    # Check square
    # First define which square we are in
    x_square = (x // 3) * 3
    y_square = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if board[x_square + i][y_square + j] == n:
                return False
    return True

def solve(bo):
    '''
    Solver for a sudoku
    :param bo: Sudoku-board to solve
    :return: A solved sudoku
    '''
    for x in range(0, 9):
        for y in range(0, 9):
            if board[x][y] == 0:
                for n in range(1, 10):
                    if valid(x,y,n):
                        board[x][y] = n
                        solve(board)
                        board[x][y] = 0
                return
    print(np.array(board))

def main():
    global board
    print("Unsolved board:")
    print(np.array(board))

    solve(board)


main()