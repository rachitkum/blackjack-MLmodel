import random

class QLearningAgent:
    def __init__(self, actions=['hit', 'stand'], learning_rate=0.1, discount_factor=0.9, exploration_rate=0.1):
        self.actions = actions  # List of actions
        self.learning_rate = learning_rate  # Learning rate (alpha)
        self.discount_factor = discount_factor  # Discount factor (gamma)
        self.exploration_rate = exploration_rate  # Exploration rate (epsilon)
        self.q_values = {}  # Dictionary to store Q-values

    def get_best_action(self, state):
        """Selects the best action based on Q-values for the given state."""
        if state not in self.q_values:
            self.q_values[state] = {action: 0.0 for action in self.actions}  # Initialize Q-values for state if not present

        if random.uniform(0, 1) < self.exploration_rate:
            # Exploration: choose a random action
            return random.choice(self.actions)
        else:
            # Exploitation: choose the best action based on Q-values
            return max(self.q_values[state], key=self.q_values[state].get)

    def update_q_values(self, state, action, reward, next_state):
        """Updates Q-values based on the Q-learning update rule."""
        if state not in self.q_values:
            self.q_values[state] = {action: 0.0 for action in self.actions}
        if next_state not in self.q_values:
            self.q_values[next_state] = {action: 0.0 for action in self.actions}

        # Q-learning formula
        best_next_action = max(self.q_values[next_state], key=self.q_values[next_state].get)
        self.q_values[state][action] += self.learning_rate * (reward + self.discount_factor * self.q_values[next_state][best_next_action] - self.q_values[state][action])
