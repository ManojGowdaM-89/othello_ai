import matplotlib.pyplot as plt
import numpy as np

# ── Results Data ──
matchups = [
    'Minimax\nvs Random',
    'Alpha-Beta\nvs Random',
    'MCTS\nvs Random',
    'Q-Learning\nvs Random',
    'Alpha-Beta\nvs Minimax',
    'MCTS\nvs Minimax',
    'Q-Learning\nvs Minimax',
    'Q-Learning\nvs Alpha-Beta',
    'Q-Learning\nvs MCTS',
    'Alpha-Beta\nvs MCTS',
]

times = [4.51, 2.89, 63.37, 8.77, 6.56, 61.94, 6.19, 1.81, 51.97, 54.4]

winners = [
    'Minimax', 'Alpha-Beta', 'MCTS', 'Q-Learning',
    'Alpha-Beta', 'Minimax', 'Minimax',
    'Alpha-Beta', 'MCTS', 'Alpha-Beta'
]

# ── Chart 1: Decision Time Comparison ──
agents = ['Minimax', 'Alpha-Beta', 'MCTS', 'Q-Learning']
agent_times = [19.24, 3.59, 89.6, 1.21]
colors = ['#1F4E79', '#2E75B6', '#7B3F8C', '#B8420A']

plt.figure(figsize=(10, 6))
bars = plt.bar(agents, agent_times, color=colors, width=0.5, edgecolor='white')
plt.title('Agent Decision Time Comparison\n(Time per game in seconds)',
          fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Agent', fontsize=12)
plt.ylabel('Time (seconds)', fontsize=12)
plt.grid(axis='y', alpha=0.3)

for bar, time in zip(bars, agent_times):
    plt.text(bar.get_x() + bar.get_width()/2,
             bar.get_height() + 1,
             f'{time}s',
             ha='center', va='bottom',
             fontweight='bold', fontsize=11)

plt.tight_layout()
plt.savefig('chart1_decision_time.png', dpi=150, bbox_inches='tight')
plt.show()
print("Chart 1 saved!")

# ── Chart 2: Tournament Results ──
agent_wins = {
    'Minimax': 0,
    'Alpha-Beta': 0,
    'MCTS': 0,
    'Q-Learning': 0,
    'Draw': 0
}

for winner in winners:
    agent_wins[winner] += 1

agents2 = ['Minimax', 'Alpha-Beta', 'MCTS', 'Q-Learning', 'Draw']
wins = [agent_wins[a] for a in agents2]
colors2 = ['#1F4E79', '#2E75B6', '#7B3F8C', '#B8420A', '#888888']

plt.figure(figsize=(10, 6))
bars2 = plt.bar(agents2, wins, color=colors2, width=0.5, edgecolor='white')
plt.title('Tournament Results — Total Wins per Agent',
          fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Agent', fontsize=12)
plt.ylabel('Number of Wins', fontsize=12)
plt.yticks(range(0, max(wins)+2))
plt.grid(axis='y', alpha=0.3)

for bar, win in zip(bars2, wins):
    plt.text(bar.get_x() + bar.get_width()/2,
             bar.get_height() + 0.05,
             str(win),
             ha='center', va='bottom',
             fontweight='bold', fontsize=12)

plt.tight_layout()
plt.savefig('chart2_tournament_wins.png', dpi=150, bbox_inches='tight')
plt.show()
print("Chart 2 saved!")

# ── Chart 3: Matchup Results Table ──
fig, ax = plt.subplots(figsize=(12, 7))
ax.axis('off')

table_data = []
for i, (matchup, winner, time) in enumerate(zip(matchups, winners, times)):
    table_data.append([
        matchup.replace('\n', ' '),
        winner,
        f'{time}s'
    ])

table = ax.table(
    cellText=table_data,
    colLabels=['Matchup', 'Winner', 'Time'],
    cellLoc='center',
    loc='center',
    bbox=[0, 0, 1, 1]
)

table.auto_set_font_size(False)
table.set_fontsize(11)

for j in range(3):
    table[0, j].set_facecolor('#1F4E79')
    table[0, j].set_text_props(color='white', fontweight='bold')

for i in range(1, len(table_data)+1):
    shade = '#EBF3FB' if i % 2 == 0 else 'white'
    for j in range(3):
        table[i, j].set_facecolor(shade)
    if table_data[i-1][1] != 'Draw':
        table[i, 1].set_text_props(color='#1F6B3A', fontweight='bold')

plt.title('Complete Tournament Results',
          fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('chart3_results_table.png', dpi=150, bbox_inches='tight')
plt.show()
print("Chart 3 saved!")

print("\nAll charts generated successfully!")
print("Files saved: chart1_decision_time.png, chart2_tournament_wins.png, chart3_results_table.png")
# ── Chart 4: Win Rate Percentage ──
agents3 = ['Minimax', 'Alpha-Beta', 'MCTS', 'Q-Learning']

# Total games played by each agent
minimax_games = 5  # vs Random, vs Alpha-Beta, vs MCTS(lost), vs Q-Learning(x2)
alphabeta_games = 5
mcts_games = 4
qlearning_games = 4

# Wins for each agent
minimax_wins = 3
alphabeta_wins = 4
mcts_wins = 2
qlearning_wins = 0

win_rates = [
    (minimax_wins / minimax_games) * 100,
    (alphabeta_wins / alphabeta_games) * 100,
    (mcts_wins / mcts_games) * 100,
    (qlearning_wins / qlearning_games) * 100,
]

colors3 = ['#1F4E79', '#2E75B6', '#7B3F8C', '#B8420A']

plt.figure(figsize=(10, 6))
bars3 = plt.bar(agents3, win_rates, color=colors3, width=0.5, edgecolor='white')
plt.title('Agent Win Rate (%)\nAcross All Tournament Matchups',
          fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Agent', fontsize=12)
plt.ylabel('Win Rate (%)', fontsize=12)
plt.ylim(0, 110)
plt.grid(axis='y', alpha=0.3)
plt.axhline(y=50, color='red', linestyle='--', alpha=0.5, label='50% line')
plt.legend()

for bar, rate in zip(bars3, win_rates):
    plt.text(bar.get_x() + bar.get_width()/2,
             bar.get_height() + 1.5,
             f'{rate:.1f}%',
             ha='center', va='bottom',
             fontweight='bold', fontsize=12)

plt.tight_layout()
plt.savefig('chart4_win_rate.png', dpi=150, bbox_inches='tight')
plt.show()
print("Chart 4 saved!")

# ── Chart 5: Speed vs Strength Scatter Plot ──
agent_names = ['Minimax', 'Alpha-Beta', 'MCTS', 'Q-Learning']
speeds = [19.24, 3.59, 89.6, 1.21]  # time in seconds
strengths = [3, 4, 2, 0]  # number of wins
colors4 = ['#1F4E79', '#2E75B6', '#7B3F8C', '#B8420A']

plt.figure(figsize=(10, 7))

for i, (name, speed, strength, color) in enumerate(
        zip(agent_names, speeds, strengths, colors4)):
    plt.scatter(speed, strength, color=color, s=300, zorder=5)
    plt.annotate(name,
                 (speed, strength),
                 textcoords="offset points",
                 xytext=(10, 5),
                 fontsize=12,
                 fontweight='bold',
                 color=color)

plt.title('Speed vs Strength Trade-off\n(Lower time = faster, Higher wins = stronger)',
          fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Decision Time per Game (seconds) — Lower is Faster', fontsize=12)
plt.ylabel('Number of Wins — Higher is Stronger', fontsize=12)
plt.grid(True, alpha=0.3)
plt.yticks(range(0, 6))

# Add quadrant labels
plt.axhline(y=2, color='grey', linestyle='--', alpha=0.3)
plt.axvline(x=20, color='grey', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.savefig('chart5_speed_vs_strength.png', dpi=150, bbox_inches='tight')
plt.show()
print("Chart 5 saved!")

print("\nAll 5 charts generated successfully!")
print("Files: chart1_decision_time.png, chart2_tournament_wins.png,")
print("       chart3_results_table.png, chart4_win_rate.png,")
print("       chart5_speed_vs_strength.png")