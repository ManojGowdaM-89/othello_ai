import time
from game.game import play_game
from agents.random_agent import random_agent
from agents.minimax_agent import minimax_agent
from agents.alphabeta_agent import alphabeta_agent
from agents.mcts_agent import mcts_agent

print("=" * 40)
print("   AI AGENTS FOR OTHELLO - COMP702")
print("=" * 40)

# Game 1 — Minimax vs Random
print("\nGame 1: Minimax vs Random...")
start = time.time()
winner1 = play_game(minimax_agent, random_agent, display=False)
time1 = round(time.time() - start, 2)

# Game 2 — Alpha-Beta vs Random
print("Game 2: Alpha-Beta vs Random...")
start = time.time()
winner2 = play_game(alphabeta_agent, random_agent, display=False)
time2 = round(time.time() - start, 2)

# Game 3 — MCTS vs Random
print("Game 3: MCTS vs Random...")
start = time.time()
winner3 = play_game(mcts_agent, random_agent, display=False)
time3 = round(time.time() - start, 2)

# Game 4 — MCTS vs Minimax
print("Game 4: MCTS vs Minimax...")
start = time.time()
winner4 = play_game(mcts_agent, minimax_agent, display=False)
time4 = round(time.time() - start, 2)

# Game 5 — MCTS vs Alpha-Beta
print("Game 5: MCTS vs Alpha-Beta...")
start = time.time()
winner5 = play_game(mcts_agent, alphabeta_agent, display=False)
time5 = round(time.time() - start, 2)

# Results Summary
print("\n" + "=" * 40)
print("         RESULTS SUMMARY")
print("=" * 40)

def get_winner_name(winner, black_name, white_name):
    if winner == 1:
        return black_name
    elif winner == 2:
        return white_name
    else:
        return "Draw"

print(f"\nGame 1 - Minimax vs Random:")
print(f"Winner: {get_winner_name(winner1, 'Minimax', 'Random')} | Time: {time1}s")

print(f"\nGame 2 - Alpha-Beta vs Random:")
print(f"Winner: {get_winner_name(winner2, 'Alpha-Beta', 'Random')} | Time: {time2}s")

print(f"\nGame 3 - MCTS vs Random:")
print(f"Winner: {get_winner_name(winner3, 'MCTS', 'Random')} | Time: {time3}s")

print(f"\nGame 4 - MCTS vs Minimax:")
print(f"Winner: {get_winner_name(winner4, 'MCTS', 'Minimax')} | Time: {time4}s")

print(f"\nGame 5 - MCTS vs Alpha-Beta:")
print(f"Winner: {get_winner_name(winner5, 'MCTS', 'Alpha-Beta')} | Time: {time5}s")

print(f"\nSpeed Comparison:")
print(f"Minimax   : {time1}s")
print(f"Alpha-Beta: {time2}s")
print(f"MCTS      : {time3}s")
print("=" * 40)