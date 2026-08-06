from game.game import play_game
from agents.random_agent import random_agent
from agents.minimax_agent import minimax_agent

print("=" * 40)
print("   AI AGENTS FOR OTHELLO - COMP702")
print("=" * 40)

# Test 1 — Minimax as Black vs Random as White
print("\nGame 1: Minimax (Black) vs Random (White)\n")
winner1 = play_game(minimax_agent, random_agent, display=True)

# Test 2 — Random as Black vs Minimax as White
print("\nGame 2: Random (Black) vs Minimax (White)\n")
winner2 = play_game(random_agent, minimax_agent, display=True)

# Summary
print("\n" + "=" * 40)
print("         RESULTS SUMMARY")
print("=" * 40)

print("\nGame 1 - Minimax (Black) vs Random (White):")
if winner1 == 1:
    print("Winner: Minimax (BLACK) ✓")
elif winner1 == 2:
    print("Winner: Random (WHITE)")
else:
    print("Draw!")

print("\nGame 2 - Random (Black) vs Minimax (White):")
if winner2 == 1:
    print("Winner: Random (BLACK)")
elif winner2 == 2:
    print("Winner: Minimax (WHITE) ✓")
else:
    print("Draw!")
print("=" * 40)