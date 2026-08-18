import time
from game.game import play_game
from agents.random_agent import random_agent
from agents.minimax_agent import minimax_agent
from agents.qlearning_agent import qlearning_agent

print("=" * 40)
print("   Q-LEARNING AGENT DEMO")
print("=" * 40)

# Q-Learning vs Random
print("\nQ-Learning vs Random...")
start = time.time()
winner1 = play_game(qlearning_agent, random_agent, display=False)
time1 = round(time.time() - start, 2)

# Q-Learning vs Minimax
print("Q-Learning vs Minimax...")
start = time.time()
winner2 = play_game(qlearning_agent, minimax_agent, display=True)
time2 = round(time.time() - start, 2)

# Results
print("\n" + "=" * 40)
print("         RESULTS")
print("=" * 40)

print(f"\nQ-Learning vs Random:")
if winner1 == 1:
    print("Q-Learning wins!")
elif winner1 == 2:
    print("Random wins!")
else:
    print("Draw!")
print(f"Time: {time1}s")

print(f"\nQ-Learning vs Minimax:")
if winner2 == 1:
    print("Q-Learning wins!")
elif winner2 == 2:
    print("Minimax wins!")
else:
    print("Draw!")
print(f"Time: {time2}s")
print("=" * 40)