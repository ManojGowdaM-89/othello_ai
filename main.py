from game.game import play_game
from agents.random_agent import random_agent

print("=" * 40)
print("   AI AGENTS FOR OTHELLO - COMP702")
print("=" * 40)
print("\nStarting game: Random vs Random\n")

# Play a game between two random agents
winner = play_game(random_agent, random_agent, display=True)

# Print final result
print("\nGame completed successfully!")
if winner == 1:
    print("Result: BLACK wins!")
elif winner == 2:
    print("Result: WHITE wins!")
else:
    print("Result: DRAW!")