import numpy as np
from game.board import BLACK, WHITE, BOARD_SIZE
from game.rules import get_valid_moves, apply_move

# Positional weights based on Rosenbloom (1982)
# Corners are most valuable, edges next to corners are dangerous
POSITION_WEIGHTS = np.array([
    [100, -20,  10,   5,   5,  10, -20, 100],
    [-20, -50,  -2,  -2,  -2,  -2, -50, -20],
    [ 10,  -2,   5,   1,   1,   5,  -2,  10],
    [  5,  -2,   1,   1,   1,   1,  -2,   5],
    [  5,  -2,   1,   1,   1,   1,  -2,   5],
    [ 10,  -2,   5,   1,   1,   5,  -2,  10],
    [-20, -50,  -2,  -2,  -2,  -2, -50, -20],
    [100, -20,  10,   5,   5,  10, -20, 100]
])

def evaluate_board(board, player):
    """
    Evaluate the board position for the given player.
    Uses positional weights based on Rosenbloom (1982).
    Positive score means player is winning.
    """
    opponent = WHITE if player == BLACK else BLACK

    # Disc count difference
    player_discs = np.sum(board == player)
    opponent_discs = np.sum(board == opponent)
    disc_score = player_discs - opponent_discs

    # Positional score
    player_position = np.sum(POSITION_WEIGHTS[board == player])
    opponent_position = np.sum(POSITION_WEIGHTS[board == opponent])
    position_score = player_position - opponent_position

    # Mobility score — number of valid moves
    player_moves = len(get_valid_moves(board, player))
    opponent_moves = len(get_valid_moves(board, opponent))
    mobility_score = player_moves - opponent_moves

    # Combined score
    return disc_score + position_score + (10 * mobility_score)

def minimax(board, depth, maximising, player, opponent):
    """
    Minimax algorithm with depth limit.
    Returns the best score for the current player.
    """
    # Base case — depth reached
    if depth == 0:
        return evaluate_board(board, player)

    current = player if maximising else opponent
    valid_moves = get_valid_moves(board, current)

    # No valid moves — pass turn
    if not valid_moves:
        # Check if opponent also has no moves — game over
        other = opponent if maximising else player
        if not get_valid_moves(board, other):
            return evaluate_board(board, player)
        # Pass turn to other player
        return minimax(board, depth - 1, not maximising, player, opponent)

    if maximising:
        best_score = float('-inf')
        for move in valid_moves:
            new_board = apply_move(board, move[0], move[1], current)
            score = minimax(new_board, depth - 1, False, player, opponent)
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for move in valid_moves:
            new_board = apply_move(board, move[0], move[1], current)
            score = minimax(new_board, depth - 1, True, player, opponent)
            best_score = min(best_score, score)
        return best_score

def minimax_agent(board, player, valid_moves, depth=3):
    """
    Minimax agent — chooses the best move using Minimax search.
    Default search depth is 3.
    """
    opponent = WHITE if player == BLACK else BLACK
    best_score = float('-inf')
    best_move = valid_moves[0]

    for move in valid_moves:
        new_board = apply_move(board, move[0], move[1], player)
        score = minimax(new_board, depth - 1, False, player, opponent)
        if score > best_score:
            best_score = score
            best_move = move

    return best_move