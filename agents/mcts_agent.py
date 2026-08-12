import math
import random
from game.board import BLACK, WHITE
from game.rules import get_valid_moves, apply_move

class MCTSNode:
    """
    Represents a node in the Monte Carlo Tree.
    Each node stores the board state, visit count,
    and win count.
    """
    def __init__(self, board, player, parent=None, move=None):
        self.board = board
        self.player = player
        self.parent = parent
        self.move = move
        self.children = []
        self.visits = 0
        self.wins = 0
        self.untried_moves = get_valid_moves(board, player)

    def is_fully_expanded(self):
        """Check if all moves have been tried."""
        return len(self.untried_moves) == 0

    def is_terminal(self):
        """Check if game is over at this node."""
        current_moves = get_valid_moves(self.board, self.player)
        opponent = WHITE if self.player == BLACK else BLACK
        opponent_moves = get_valid_moves(self.board, opponent)
        return len(current_moves) == 0 and len(opponent_moves) == 0

    def ucb1(self, exploration=1.414):
        """
        UCB1 formula for node selection.
        Balances exploitation and exploration.
        UCB1 = wins/visits + C * sqrt(ln(parent visits) / visits)
        """
        if self.visits == 0:
            return float('inf')
        return (self.wins / self.visits) + exploration * math.sqrt(
            math.log(self.parent.visits) / self.visits)

    def best_child(self):
        """Select child with highest UCB1 score."""
        if not self.children:
            return None
        return max(self.children, key=lambda c: c.ucb1())

    def expand(self):
        """Expand node by adding one untried move."""
        move = self.untried_moves.pop()
        opponent = WHITE if self.player == BLACK else BLACK
        new_board = apply_move(self.board, move[0], move[1], self.player)
        child = MCTSNode(new_board, opponent, parent=self, move=move)
        self.children.append(child)
        return child

    def simulate(self, original_player):
        """
        Simulate a random game from this node.
        Returns 1 if original player wins, 0 otherwise.
        """
        board = self.board.copy()
        current = self.player
        pass_count = 0

        while True:
            moves = get_valid_moves(board, current)
            if not moves:
                pass_count += 1
                if pass_count >= 2:
                    break
                current = WHITE if current == BLACK else BLACK
                continue
            pass_count = 0
            move = random.choice(moves)
            board = apply_move(board, move[0], move[1], current)
            current = WHITE if current == BLACK else BLACK

        # Count discs to determine winner
        from game.board import get_score
        black_score, white_score = get_score(board)
        if original_player == BLACK:
            return 1 if black_score > white_score else 0
        else:
            return 1 if white_score > black_score else 0

    def backpropagate(self, result):
        """Update visit count and win count up the tree."""
        self.visits += 1
        self.wins += result
        if self.parent:
            self.parent.backpropagate(result)


def mcts_agent(board, player, valid_moves, simulations=500):
    """
    MCTS agent — chooses the best move using
    Monte Carlo Tree Search.
    Uses 500 simulations per move by default.
    Four stages: Selection, Expansion,
    Simulation, Backpropagation.
    """
    # Create root node
    root = MCTSNode(board, player)

    # Run simulations
    for _ in range(simulations):
        node = root

        # Stage 1 — Selection
        while node.is_fully_expanded() and not node.is_terminal():
            best = node.best_child()
            if best is None:
                break
            node = best

        # Stage 2 — Expansion
        if not node.is_fully_expanded() and not node.is_terminal():
            node = node.expand()

        # Stage 3 — Simulation
        result = node.simulate(player)

        # Stage 4 — Backpropagation
        node.backpropagate(result)

    # Choose move with most visits
    if not root.children:
        return valid_moves[0]
    best_child = max(root.children, key=lambda c: c.visits)
    return best_child.move