import random

def random_agent(board, player, valid_moves):
    """
    Random agent — picks a random valid move.
    Used for testing the game engine.
    """
    return random.choice(valid_moves)