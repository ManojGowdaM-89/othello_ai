from game.board import (create_board, print_board, 
                        get_score, is_full, BLACK, WHITE)
from game.rules import get_valid_moves, apply_move

def play_game(black_agent, white_agent, display=True):
    """
    Play a complete game between two agents.
    Returns the winner: BLACK, WHITE, or None for draw.
    """
    board = create_board()
    current_player = BLACK
    pass_count = 0

    if display:
        print("=" * 40)
        print("       OTHELLO GAME START")
        print("=" * 40)
        print_board(board)

    while True:
        valid_moves = get_valid_moves(board, current_player)

        # No valid moves — pass turn
        if not valid_moves:
            pass_count += 1
            if display:
                player_name = "BLACK" if current_player == BLACK else "WHITE"
                print(f"{player_name} has no valid moves — passing turn.")

            # Both players have no moves — game over
            if pass_count >= 2:
                break

            # Switch player
            current_player = WHITE if current_player == BLACK else BLACK
            continue

        # Reset pass count since a move was made
        pass_count = 0

        # Get move from agent
        if current_player == BLACK:
            move = black_agent(board, current_player, valid_moves)
        else:
            move = white_agent(board, current_player, valid_moves)

        # Apply the move
        board = apply_move(board, move[0], move[1], current_player)

        if display:
            player_name = "BLACK" if current_player == BLACK else "WHITE"
            col_letter = chr(move[1] + ord('A'))
            print(f"{player_name} plays at {col_letter}{move[0] + 1}")
            print_board(board)

        # Check if board is full
        if is_full(board):
            break

        # Switch player
        current_player = WHITE if current_player == BLACK else BLACK

    # Calculate final score
    black_score, white_score = get_score(board)

    if display:
        print("=" * 40)
        print("           GAME OVER")
        print("=" * 40)
        print(f"Black: {black_score} discs")
        print(f"White: {white_score} discs")

        if black_score > white_score:
            print("Winner: BLACK!")
        elif white_score > black_score:
            print("Winner: WHITE!")
        else:
            print("It's a DRAW!")
        print("=" * 40)

    # Return winner
    if black_score > white_score:
        return BLACK
    elif white_score > black_score:
        return WHITE
    else:
        return None