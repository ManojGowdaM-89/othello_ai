import random
import pickle
import os
from game.board import BLACK, WHITE
from game.rules import get_valid_moves, apply_move
from game.board import get_score

# Q-Learning parameters
LEARNING_RATE = 0.1       # Alpha — how fast agent learns
DISCOUNT_FACTOR = 0.9     # Gamma — importance of future rewards
EPSILON_START = 1.0       # Start with full exploration
EPSILON_END = 0.1         # Minimum exploration rate
EPSILON_DECAY = 0.995     # How fast exploration decreases
TRAINING_GAMES = 1000     # Number of self-play training games

def get_state(board, player):
    """
    Convert board to a simplified state representation.
    Uses tuple of board values as dictionary key.
    """
    return (tuple(board.flatten()), player)

def get_reward(board, player):
    """
    Calculate reward for the current board state.
    Win = +1, Loss = -1, Draw = 0
    """
    black_score, white_score = get_score(board)
    if player == BLACK:
        if black_score > white_score:
            return 1
        elif black_score < white_score:
            return -1
        else:
            return 0
    else:
        if white_score > black_score:
            return 1
        elif white_score < black_score:
            return -1
        else:
            return 0

class QLearningAgent:
    """
    Basic Q-Learning agent for Othello.
    Uses a Q-table stored as a dictionary.
    State = board configuration + player
    Action = move position (row, col)
    """
    def __init__(self):
        self.q_table = {}
        self.epsilon = EPSILON_START

    def get_q_value(self, state, move):
        """Get Q-value for state-action pair."""
        return self.q_table.get((state, move), 0.0)

    def choose_move(self, board, player, valid_moves):
        """
        Choose move using epsilon-greedy policy.
        Explore randomly with probability epsilon.
        Exploit best known move otherwise.
        """
        # Exploration — random move
        if random.random() < self.epsilon:
            return random.choice(valid_moves)

        # Exploitation — best known move
        state = get_state(board, player)
        best_move = valid_moves[0]
        best_value = float('-inf')

        for move in valid_moves:
            q_value = self.get_q_value(state, move)
            if q_value > best_value:
                best_value = q_value
                best_move = move

        return best_move

    def update(self, state, move, reward, next_board, next_player, next_moves):
        """
        Update Q-table using Bellman equation:
        Q(s,a) = Q(s,a) + alpha * (r + gamma * max Q(s',a') - Q(s,a))
        """
        current_q = self.get_q_value(state, move)

        # Get maximum Q-value for next state
        if next_moves:
            next_state = get_state(next_board, next_player)
            max_next_q = max(
                self.get_q_value(next_state, m) for m in next_moves
            )
        else:
            max_next_q = 0.0

        # Bellman equation update
        new_q = current_q + LEARNING_RATE * (
            reward + DISCOUNT_FACTOR * max_next_q - current_q
        )
        self.q_table[(state, move)] = new_q

    def decay_epsilon(self):
        """Decay epsilon after each game."""
        self.epsilon = max(EPSILON_END, self.epsilon * EPSILON_DECAY)

    def save(self, filepath="agents/q_table.pkl"):
        """Save Q-table to file."""
        with open(filepath, 'wb') as f:
            pickle.dump(self.q_table, f)
        print(f"Q-table saved — {len(self.q_table)} state-action pairs")

    def load(self, filepath="agents/q_table.pkl"):
        """Load Q-table from file."""
        if os.path.exists(filepath):
            with open(filepath, 'rb') as f:
                self.q_table = pickle.load(f)
            print(f"Q-table loaded — {len(self.q_table)} state-action pairs")
            return True
        return False


def train_qlearning(games=TRAINING_GAMES):
    """
    Train Q-Learning agent through self-play.
    Agent plays against itself for specified number of games.
    """
    agent = QLearningAgent()
    print(f"Training Q-Learning agent for {games} games...")

    for game_num in range(games):
        # Print progress every 100 games
        if (game_num + 1) % 100 == 0:
            print(f"Training game {game_num + 1}/{games} | Epsilon: {agent.epsilon:.3f}")

        from game.board import create_board
        board = create_board()
        current_player = BLACK
        pass_count = 0

        while True:
            valid_moves = get_valid_moves(board, current_player)

            if not valid_moves:
                pass_count += 1
                if pass_count >= 2:
                    break
                current_player = WHITE if current_player == BLACK else BLACK
                continue

            pass_count = 0
            state = get_state(board, current_player)
            move = agent.choose_move(board, current_player, valid_moves)
            new_board = apply_move(board, move[0], move[1], current_player)

            # Get next player and moves
            next_player = WHITE if current_player == BLACK else BLACK
            next_moves = get_valid_moves(new_board, next_player)

            # Calculate reward only at game end
            reward = 0
            if not next_moves:
                other_moves = get_valid_moves(new_board, current_player)
                if not other_moves:
                    reward = get_reward(new_board, current_player)

            # Update Q-table
            agent.update(state, move, reward, new_board, next_player, next_moves)

            board = new_board
            current_player = next_player

        agent.decay_epsilon()

    agent.save()
    print(f"Training complete!")
    return agent


# Global agent instance
_trained_agent = None

def qlearning_agent(board, player, valid_moves):
    """
    Q-Learning agent — uses trained Q-table to choose moves.
    Trains automatically if no saved Q-table exists.
    """
    global _trained_agent

    if _trained_agent is None:
        _trained_agent = QLearningAgent()
        # Try to load existing Q-table
        if not _trained_agent.load():
            # Train if no saved table
            _trained_agent = train_qlearning()
        # Set epsilon to 0 for pure exploitation during play
        _trained_agent.epsilon = 0.0

    return _trained_agent.choose_move(board, player, valid_moves)