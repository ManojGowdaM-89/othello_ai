import numpy as np

# Board constants
EMPTY = 0
BLACK = 1
WHITE = 2
BOARD_SIZE = 8

def create_board():
    # sets up 8*8 board with 4 starting discs in centre
    board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
    # Starting position - 4 discs in the centre
    board[3][3] = WHITE
    board[3][4] = BLACK
    board[4][3] = BLACK
    board[4][4] = WHITE
    return board

def print_board(board):
    # prints the board with column letters and row numbers
    print("\n  A B C D E F G H")
    print("  ----------------")
    for row in range(BOARD_SIZE):
        print(f"{row + 1}|", end=" ")
        for col in range(BOARD_SIZE):
            if board[row][col] == EMPTY:
                print(".", end=" ")
            elif board[row][col] == BLACK:
                print("B", end=" ")
            else:
                print("W", end=" ")
        print()
    print()

def get_score(board):
    # Count discs for each players and returns scores
    black = np.sum(board == BLACK)
    white = np.sum(board == WHITE)
    return int(black), int(white)

def is_full(board):
   # returns true if no empty squares remain
    return not np.any(board == EMPTY)