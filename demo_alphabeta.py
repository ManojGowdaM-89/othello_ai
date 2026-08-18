import time
from game.game import play_game
from agents.random_agent import random_agent
from agents.minimax_agent import minimax_agent
from agents.alphabeta_agent import alphabeta_agent

print("=" * 40)
print("   ALPHA-BETA PRUNING vs MINIMAX")
print("=" * 40)

# Speed comparison
print("\nTesting Minimax speed...")
start = time.time()
winner1 = play_game(minimax_agent, random_agent, display=False)
minimax_time = round(time.time() - start, 2)

print("Testing Alpha-Beta speed...")
start = time.time()
winner2 = play_game(alphabeta_agent, random_agent, display=False)
ab_time = round(time.time() - start, 2)

# Head to head
print("\nHead to head — Alpha-Beta vs Minimax...")
start = time.time()
winner3 = play_game(alphabeta_agent, minimax_agent, display=True)
h2h_time = round(time.time() - start, 2)

# Results
print("\n" + "=" * 40)
print("         RESULTS")
print("=" * 40)
print(f"\nMinimax time   : {minimax_time}s")
print(f"Alpha-Beta time: {ab_time}s")
print(f"Speed improvement: {round(minimax_time/ab_time, 2)}x faster!")
print(f"\nHead to Head result:")
if winner3 == 1:
    print("Alpha-Beta (BLACK) wins!")
elif winner3 == 2:
    print("Minimax (WHITE) wins!")
else:
    print("Draw!")
print("=" * 40)