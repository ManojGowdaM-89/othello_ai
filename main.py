import time
from game.game import play_game
from agents.random_agent import random_agent
from agents.minimax_agent import minimax_agent
from agents.alphabeta_agent import alphabeta_agent
from agents.mcts_agent import mcts_agent
from agents.qlearning_agent import qlearning_agent, train_qlearning

print("=" * 40)
print("   AI AGENTS FOR OTHELLO - COMP702")
print("=" * 40)

# Train Q-Learning agent first
print("\nTraining Q-Learning agent...")
train_qlearning(games=1000)

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

# Game 4 — Q-Learning vs Random
print("Game 4: Q-Learning vs Random...")
start = time.time()
winner4 = play_game(qlearning_agent, random_agent, display=False)
time4 = round(time.time() - start, 2)

# Game 5 — Alpha-Beta vs Minimax
print("Game 5: Alpha-Beta vs Minimax...")
start = time.time()
winner5 = play_game(alphabeta_agent, minimax_agent, display=False)
time5 = round(time.time() - start, 2)

# Game 6 — MCTS vs Minimax
print("Game 6: MCTS vs Minimax...")
start = time.time()
winner6 = play_game(mcts_agent, minimax_agent, display=False)
time6 = round(time.time() - start, 2)

# Game 7 — Q-Learning vs Minimax
print("Game 7: Q-Learning vs Minimax...")
start = time.time()
winner7 = play_game(qlearning_agent, minimax_agent, display=False)
time7 = round(time.time() - start, 2)

# Game 8 — Q-Learning vs Alpha-Beta
print("Game 8: Q-Learning vs Alpha-Beta...")
start = time.time()
winner8 = play_game(qlearning_agent, alphabeta_agent, display=False)
time8 = round(time.time() - start, 2)

# Game 9 — Q-Learning vs MCTS
print("Game 9: Q-Learning vs MCTS...")
start = time.time()
winner9 = play_game(qlearning_agent, mcts_agent, display=False)
time9 = round(time.time() - start, 2)

# Game 10 — Alpha-Beta vs MCTS
print("Game 10: Alpha-Beta vs MCTS...")
start = time.time()
winner10 = play_game(alphabeta_agent, mcts_agent, display=False)
time10 = round(time.time() - start, 2)

# Results Summary
print("\n" + "=" * 40)
print("         RESULTS SUMMARY")
print("=" * 40)

def result(winner, black_name, white_name):
    if winner == 1:
        return f"{black_name} wins"
    elif winner == 2:
        return f"{white_name} wins"
    else:
        return "Draw"

print(f"\nGame 1 - Minimax vs Random      : {result(winner1, 'Minimax', 'Random')} | {time1}s")
print(f"Game 2 - Alpha-Beta vs Random   : {result(winner2, 'Alpha-Beta', 'Random')} | {time2}s")
print(f"Game 3 - MCTS vs Random         : {result(winner3, 'MCTS', 'Random')} | {time3}s")
print(f"Game 4 - Q-Learning vs Random   : {result(winner4, 'Q-Learning', 'Random')} | {time4}s")
print(f"Game 5 - Alpha-Beta vs Minimax  : {result(winner5, 'Alpha-Beta', 'Minimax')} | {time5}s")
print(f"Game 6 - MCTS vs Minimax        : {result(winner6, 'MCTS', 'Minimax')} | {time6}s")
print(f"Game 7 - Q-Learning vs Minimax  : {result(winner7, 'Q-Learning', 'Minimax')} | {time7}s")
print(f"Game 8  - Q-Learning vs Alpha-Beta : {result(winner8, 'Q-Learning', 'Alpha-Beta')} | {time8}s")
print(f"Game 9  - Q-Learning vs MCTS       : {result(winner9, 'Q-Learning', 'MCTS')} | {time9}s")
print(f"Game 10 - Alpha-Beta vs MCTS       : {result(winner10, 'Alpha-Beta', 'MCTS')} | {time10}s")
print(f"\nSpeed Comparison:")
print(f"Minimax    : {time1}s")
print(f"Alpha-Beta : {time2}s")
print(f"MCTS       : {time3}s")
print(f"Q-Learning : {time4}s")
print("=" * 40)