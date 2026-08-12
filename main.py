import time
from game.game import play_game
from agents.random_agent import random_agent
from agents.minimax_agent import minimax_agent
from agents.alphabeta_agent import alphabeta_agent

print("=" * 40)
print("   AI AGENTS FOR OTHELLO - COMP702")
print("=" * 40)

# Game 1 — Minimax vs Random
print("\nGame 1: Minimax (Black) vs Random (White)\n")
start = time.time()
winner1 = play_game(minimax_agent, random_agent, display=False)
time1 = round(time.time() - start, 2)

# Game 2 — Alpha-Beta vs Random
print("Game 2: Alpha-Beta (Black) vs Random (White)\n")
start = time.time()
winner2 = play_game(alphabeta_agent, random_agent, display=False)
time2 = round(time.time() - start, 2)

# Game 3 — Alpha-Beta vs Minimax
print("Game 3: Alpha-Beta (Black) vs Minimax (White)\n")
start = time.time()
winner3 = play_game(alphabeta_agent, minimax_agent, display=False)
time3 = round(time.time() - start, 2)

# Results Summary
print("\n" + "=" * 40)
print("         RESULTS SUMMARY")
print("=" * 40)

print(f"\nGame 1 - Minimax vs Random:")
print(f"Winner: {'Minimax' if winner1 == 1 else 'Random' if winner1 == 2 else 'Draw'}")
print(f"Time: {time1} seconds")

print(f"\nGame 2 - Alpha-Beta vs Random:")
print(f"Winner: {'Alpha-Beta' if winner2 == 1 else 'Random' if winner2 == 2 else 'Draw'}")
print(f"Time: {time2} seconds")

print(f"\nGame 3 - Alpha-Beta vs Minimax:")
print(f"Winner: {'Alpha-Beta' if winner3 == 1 else 'Minimax' if winner3 == 2 else 'Draw'}")
print(f"Time: {time3} seconds")

print(f"\nSpeed Comparison:")
print(f"Minimax  : {time1} seconds")
print(f"Alpha-Beta: {time2} seconds")
if time2 < time1:
    print(f"Alpha-Beta is {round(time1/time2, 2)}x faster than Minimax!")
print("=" * 40)