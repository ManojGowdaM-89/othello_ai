import numpy as np

# Board constants
EMPTY = 0
BLACK = 1
WHITE = 2
BOARD_SIZE = 8

def create_board():
    """Create and return a new Othello board with starting position."""
    board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
    # Starting position - 4 discs in the centre
    board[3][3] = WHITE
    board[3][4] = BLACK
    board[4][3] = BLACK
    board[4][4] = WHITE
    return board

def print_board(board):
    """Print the board in a readable format."""
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
    """Return the score as (black_count, white_count)."""
    black = np.sum(board == BLACK)
    white = np.sum(board == WHITE)
    return int(black), int(white)

def is_full(board):
    """Check if the board is full."""
    return not np.any(board == EMPTY)