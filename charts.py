import matplotlib.pyplot as plt
import numpy as np

# ── Updated Results Data — 100 Tournaments x 2 Games ──

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

# Win rates for black agent in each matchup
win_rates = [95.5, 95.0, 97.0, 55.5, 100.0, 16.5, 0.0, 0.0, 12.0, 71.0]

# Average time per game
times_per_game = [131.92, 3.76, 7.61, 0.15, 64.85, 62.1, 118.33, 57.21, 62.43, 297.13]

# Agent overall wins
agents = ['Minimax', 'Alpha-Beta', 'MCTS', 'Q-Learning']
agent_wins = [3, 4, 2, 0]
agent_times = [131.92, 3.76, 7.61, 0.15]
colors = ['#1F4E79', '#2E75B6', '#7B3F8C', '#B8420A']

# ── Chart 1: Decision Time Comparison ──
plt.figure(figsize=(10, 6))
bars = plt.bar(agents, agent_times, color=colors, width=0.5, edgecolor='white')
plt.title('Agent Average Decision Time\n(Average time per game in seconds)',
          fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Agent', fontsize=12)
plt.ylabel('Average Time per Game (seconds)', fontsize=12)
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

# ── Chart 2: Tournament Wins ──
plt.figure(figsize=(10, 6))
bars2 = plt.bar(agents, agent_wins, color=colors, width=0.5, edgecolor='white')
plt.title('Tournament Results — Total Wins per Agent\n(200 games per matchup)',
          fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Agent', fontsize=12)
plt.ylabel('Number of Matchups Won', fontsize=12)
plt.yticks(range(0, 6))
plt.grid(axis='y', alpha=0.3)
for bar, win in zip(bars2, agent_wins):
    plt.text(bar.get_x() + bar.get_width()/2,
             bar.get_height() + 0.05,
             str(win),
             ha='center', va='bottom',
             fontweight='bold', fontsize=12)
plt.tight_layout()
plt.savefig('chart2_tournament_wins.png', dpi=150, bbox_inches='tight')
plt.show()
print("Chart 2 saved!")

# ── Chart 3: Results Table ──
fig, ax = plt.subplots(figsize=(14, 7))
ax.axis('off')
table_data = [
    ['Minimax vs Random', '191/200', '6/200', '3/200', '95.5%', '131.92s'],
    ['Alpha-Beta vs Random', '190/200', '4/200', '6/200', '95.0%', '3.76s'],
    ['MCTS vs Random', '194/200', '4/200', '2/200', '97.0%', '7.61s'],
    ['Q-Learning vs Random', '111/200', '85/200', '4/200', '55.5%', '0.15s'],
    ['Alpha-Beta vs Minimax', '200/200', '0/200', '0/200', '100.0%', '64.85s'],
    ['MCTS vs Minimax', '33/200', '164/200', '3/200', '16.5%', '62.1s'],
    ['Q-Learning vs Minimax', '0/200', '200/200', '0/200', '0.0%', '118.33s'],
    ['Q-Learning vs Alpha-Beta', '0/200', '200/200', '0/200', '0.0%', '57.21s'],
    ['Q-Learning vs MCTS', '24/200', '175/200', '1/200', '12.0%', '62.43s'],
    ['Alpha-Beta vs MCTS', '142/200', '56/200', '2/200', '71.0%', '297.13s'],
]
table = ax.table(
    cellText=table_data,
    colLabels=['Matchup', 'Black Wins', 'White Wins', 'Draws', 'Black Win%', 'Avg Time'],
    cellLoc='center',
    loc='center',
    bbox=[0, 0, 1, 1]
)
table.auto_set_font_size(False)
table.set_fontsize(10)
for j in range(6):
    table[0, j].set_facecolor('#1F4E79')
    table[0, j].set_text_props(color='white', fontweight='bold')
for i in range(1, len(table_data)+1):
    shade = '#EBF3FB' if i % 2 == 0 else 'white'
    for j in range(6):
        table[i, j].set_facecolor(shade)
plt.title('Complete Tournament Results\n(100 Tournaments x 2 Games = 200 games per matchup)',
          fontsize=13, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('chart3_results_table.png', dpi=150, bbox_inches='tight')
plt.show()
print("Chart 3 saved!")

# ── Chart 4: Win Rate ──
win_rate_vals = [95.5, 95.0, 97.0, 55.5]
plt.figure(figsize=(10, 6))
bars3 = plt.bar(agents, win_rate_vals, color=colors, width=0.5, edgecolor='white')
plt.title('Agent Win Rate vs Random Agent\n(200 games per matchup)',
          fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Agent', fontsize=12)
plt.ylabel('Win Rate (%)', fontsize=12)
plt.ylim(0, 115)
plt.grid(axis='y', alpha=0.3)
plt.axhline(y=50, color='red', linestyle='--', alpha=0.5, label='50% baseline')
plt.legend()
for bar, rate in zip(bars3, win_rate_vals):
    plt.text(bar.get_x() + bar.get_width()/2,
             bar.get_height() + 1.5,
             f'{rate}%',
             ha='center', va='bottom',
             fontweight='bold', fontsize=12)
plt.tight_layout()
plt.savefig('chart4_win_rate.png', dpi=150, bbox_inches='tight')
plt.show()
print("Chart 4 saved!")

# ── Chart 5: Speed vs Strength ──
strengths = [3, 4, 2, 0]
plt.figure(figsize=(10, 7))
for i, (name, speed, strength, color) in enumerate(
        zip(agents, agent_times, strengths, colors)):
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
plt.xlabel('Average Decision Time per Game (seconds)', fontsize=12)
plt.ylabel('Number of Matchups Won', fontsize=12)
plt.grid(True, alpha=0.3)
plt.yticks(range(0, 6))
plt.tight_layout()
plt.savefig('chart5_speed_vs_strength.png', dpi=150, bbox_inches='tight')
plt.show()
print("Chart 5 saved!")

print("\nAll 5 charts updated successfully!")