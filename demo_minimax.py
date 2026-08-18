from game.game import play_game
from agents.random_agent import random_agent
from agents.minimax_agent import minimax_agent

print("=" * 40)
print("   MINIMAX vs RANDOM")
print("=" * 40)

winner = play_game(minimax_agent, random_agent, display=True)

print("\nFinal Result:")
if winner == 1:
    print("Minimax (BLACK) wins!")
elif winner == 2:
    print("Random (WHITE) wins!")
else:
    print("Draw!")