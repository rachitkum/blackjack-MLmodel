import pickle
import random

class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.q_table = {}  # Q-values for state-action pairs
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor
        self.epsilon = epsilon  # Exploration rate

    def get_best_action(self, state):
        # Epsilon-greedy action selection
        if random.random() < self.epsilon or state not in self.q_table:
            return random.choice(["hit", "stand"])
        return max(self.q_table[state], key=self.q_table[state].get)

    def get_win_probability(self, state, action):
        # Calculate win probability for a given state-action pair
        if state in self.q_table and action in self.q_table[state]:
            q_value = self.q_table[state][action]
            return max(0, min(1, (q_value + 1) / 2))  # Scale Q-value to [0, 1]
        return 0.5  # Default probability for unknown state-action pairs

    def update_q_values(self, state, action, reward, next_state):
        # Initialize state in Q-table
        if state not in self.q_table:
            self.q_table[state] = {a: 0 for a in ["hit", "stand"]}

        # Update Q-value for the state-action pair
        next_max = max(self.q_table.get(next_state, {a: 0 for a in ["hit", "stand"]}).values())
        self.q_table[state][action] += self.alpha * (reward + self.gamma * next_max - self.q_table[state][action])

    def save(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def load(cls, filename):
        with open(filename, "rb") as file:
            return pickle.load(file)
