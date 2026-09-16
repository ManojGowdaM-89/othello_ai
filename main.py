import time
from game.game import play_game
from agents.random_agent import random_agent
from agents.minimax_agent import minimax_agent
from agents.alphabeta_agent import alphabeta_agent
from agents.mcts_agent import mcts_agent
from agents.qlearning_agent import qlearning_agent

# Tournament settings
GAMES_PER_MATCHUP = 2
TOURNAMENTS = 100

print("=" * 50)
print("   AI AGENTS FOR OTHELLO - COMP702")
print(f"   {TOURNAMENTS} Tournaments x {GAMES_PER_MATCHUP} Games per Matchup")
print("=" * 50)

# Define matchups
matchups = [
    ("Minimax", minimax_agent, "Random", random_agent),
    ("Alpha-Beta", alphabeta_agent, "Random", random_agent),
    ("MCTS", mcts_agent, "Random", random_agent),
    ("Q-Learning", qlearning_agent, "Random", random_agent),
    ("Alpha-Beta", alphabeta_agent, "Minimax", minimax_agent),
    ("MCTS", mcts_agent, "Minimax", minimax_agent),
    ("Q-Learning", qlearning_agent, "Minimax", minimax_agent),
    ("Q-Learning", qlearning_agent, "Alpha-Beta", alphabeta_agent),
    ("Q-Learning", qlearning_agent, "MCTS", mcts_agent),
    ("Alpha-Beta", alphabeta_agent, "MCTS", mcts_agent),
]

# Results storage
results = {f"{b} vs {w}": {"black_wins": 0, "white_wins": 0, "draws": 0, "total_time": 0}
           for b, _, w, _ in matchups}

total_start = time.time()

for tournament in range(1, TOURNAMENTS + 1):
    print(f"\nTournament {tournament}/{TOURNAMENTS}...")
    for black_name, black_agent, white_name, white_agent in matchups:
        key = f"{black_name} vs {white_name}"
        for game in range(GAMES_PER_MATCHUP):
            start = time.time()
            winner = play_game(black_agent, white_agent, display=False)
            elapsed = time.time() - start
            results[key]["total_time"] += elapsed
            if winner == 1:
                results[key]["black_wins"] += 1
            elif winner == 2:
                results[key]["white_wins"] += 1
            else:
                results[key]["draws"] += 1

total_time = round(time.time() - total_start, 2)
total_games = TOURNAMENTS * GAMES_PER_MATCHUP

print("\n" + "=" * 50)
print("         FINAL RESULTS SUMMARY")
print(f"   {TOURNAMENTS} Tournaments x {GAMES_PER_MATCHUP} Games = {total_games} games per matchup")
print("=" * 50)

for black_name, _, white_name, _ in matchups:
    key = f"{black_name} vs {white_name}"
    r = results[key]
    total = r["black_wins"] + r["white_wins"] + r["draws"]
    black_rate = round((r["black_wins"] / total) * 100, 1)
    white_rate = round((r["white_wins"] / total) * 100, 1)
    draw_rate = round((r["draws"] / total) * 100, 1)
    avg_time = round(r["total_time"] / total, 2)
    print(f"\n{key}:")
    print(f"  {black_name} wins: {r['black_wins']}/{total} ({black_rate}%)")
    print(f"  {white_name} wins: {r['white_wins']}/{total} ({white_rate}%)")
    print(f"  Draws: {r['draws']}/{total} ({draw_rate}%)")
    print(f"  Avg time per game: {avg_time}s")

print(f"\nTotal time: {total_time}s")
print("=" * 50)