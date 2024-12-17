# q_learning/q_learning.py
import pickle
import random

class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor
        self.epsilon = epsilon  # Exploration rate
        self.q_table = {}

    def get_best_action(self, state):
        """Get the best action for the current state."""
        if state not in self.q_table or random.random() < self.epsilon:
            return random.choice(['hit', 'stand'])
        return max(self.q_table[state], key=self.q_table[state].get)

    def update_q_values(self, state, action, reward, next_state):
        """Update Q-values using the Q-learning formula."""
        if state not in self.q_table:
            self.q_table[state] = {'hit': 0, 'stand': 0}

        max_next_q = max(self.q_table[next_state].values()) if next_state in self.q_table else 0
        self.q_table[state][action] += self.alpha * (reward + self.gamma * max_next_q - self.q_table[state][action])

    def save(self, filename):
        """Save the Q-learning agent to a file."""
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load(filename):
        """Load the Q-learning agent from a file."""
        with open(filename, 'rb') as file:
            return pickle.load(file)
