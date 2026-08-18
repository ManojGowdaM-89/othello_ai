import time
from game.game import play_game
from agents.random_agent import random_agent
from agents.minimax_agent import minimax_agent
from agents.mcts_agent import mcts_agent

print("=" * 40)
print("   MCTS vs RANDOM and MINIMAX")
print("=" * 40)

# MCTS vs Random
print("\nMCTS vs Random...")
start = time.time()
winner1 = play_game(mcts_agent, random_agent, display=False)
time1 = round(time.time() - start, 2)

# MCTS vs Minimax
print("MCTS vs Minimax...")
start = time.time()
winner2 = play_game(mcts_agent, minimax_agent, display=True)
time2 = round(time.time() - start, 2)

# Results
print("\n" + "=" * 40)
print("         RESULTS")
print("=" * 40)

print(f"\nMCTS vs Random:")
if winner1 == 1:
    print("MCTS wins!")
elif winner1 == 2:
    print("Random wins!")
else:
    print("Draw!")
print(f"Time: {time1}s")

print(f"\nMCTS vs Minimax:")
if winner2 == 1:
    print("MCTS wins!")
elif winner2 == 2:
    print("Minimax wins!")
else:
    print("Draw!")
print(f"Time: {time2}s")
print("=" * 40)