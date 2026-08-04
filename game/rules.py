from game.board import EMPTY, BLACK, WHITE, BOARD_SIZE

# All 8 directions: up, down, left, right and 4 diagonals
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1),
              (-1, -1), (-1, 1), (1, -1), (1, 1)]

def is_valid_move(board, row, col, player):
    """Check if placing a disc at (row, col) is valid for player."""
    if board[row][col] != EMPTY:
        return False

    opponent = WHITE if player == BLACK else BLACK

    for dr, dc in DIRECTIONS:
        r, c = row + dr, col + dc
        found_opponent = False

        while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE:
            if board[r][c] == opponent:
                found_opponent = True
            elif board[r][c] == player:
                if found_opponent:
                    return True
                break
            else:
                break
            r += dr
            c += dc

    return False

def get_valid_moves(board, player):
    """Return a list of all valid moves for player."""
    valid_moves = []
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if is_valid_move(board, row, col, player):
                valid_moves.append((row, col))
    return valid_moves

def apply_move(board, row, col, player):
    """Apply a move and flip all captured discs. Returns new board."""
    new_board = board.copy()
    new_board[row][col] = player
    opponent = WHITE if player == BLACK else BLACK

    for dr, dc in DIRECTIONS:
        r, c = row + dr, col + dc
        discs_to_flip = []

        while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE:
            if new_board[r][c] == opponent:
                discs_to_flip.append((r, c))
            elif new_board[r][c] == player:
                for fr, fc in discs_to_flip:
                    new_board[fr][fc] = player
                break
            else:
                break
            r += dr
            c += dc

    return new_board

def get_opponent(player):
    """Return the opponent of the given player."""
    return WHITE if player == BLACK else BLACK