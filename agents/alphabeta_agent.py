import numpy as np
from game.board import BLACK, WHITE, BOARD_SIZE
from game.rules import get_valid_moves, apply_move
from agents.minimax_agent import evaluate_board

def alphabeta(board, depth, alpha, beta, maximising, player, opponent):
    """
    Alpha-Beta Pruning algorithm.
    Produces identical results to Minimax but faster
    by pruning irrelevant branches.
    alpha = best value for maximising player
    beta = best value for minimising player
    """
    # Base case — depth reached
    if depth == 0:
        return evaluate_board(board, player)

    current = player if maximising else opponent
    valid_moves = get_valid_moves(board, current)

    # No valid moves — pass turn
    if not valid_moves:
        other = opponent if maximising else player
        if not get_valid_moves(board, other):
            return evaluate_board(board, player)
        return alphabeta(board, depth - 1, alpha, beta, not maximising, player, opponent)

    if maximising:
        best_score = float('-inf')
        for move in valid_moves:
            new_board = apply_move(board, move[0], move[1], current)
            score = alphabeta(new_board, depth - 1, alpha, beta, False, player, opponent)
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            # Prune — beta cutoff
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = float('inf')
        for move in valid_moves:
            new_board = apply_move(board, move[0], move[1], current)
            score = alphabeta(new_board, depth - 1, alpha, beta, True, player, opponent)
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            # Prune — alpha cutoff
            if beta <= alpha:
                break
        return best_score

def alphabeta_agent(board, player, valid_moves, depth=3):
    """
    Alpha-Beta Pruning agent — chooses the best move
    using Alpha-Beta search. Produces same results as
    Minimax but significantly faster.
    Default search depth is 3.
    """
    opponent = WHITE if player == BLACK else BLACK
    best_score = float('-inf')
    best_move = valid_moves[0]
    alpha = float('-inf')
    beta = float('inf')

    for move in valid_moves:
        new_board = apply_move(board, move[0], move[1], player)
        score = alphabeta(new_board, depth - 1, alpha, beta, False, player, opponent)
        if score > best_score:
            best_score = score
            best_move = move
        alpha = max(alpha, best_score)

    return best_move