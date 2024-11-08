import pandas as pd
from q_learning.q_learning import QLearningAgent
from game.blackjack_game import BlackjackGame

def train_agent(data, episodes=1000):
    # Initialize the Q-learning agent
    q_learning_agent = QLearningAgent()

    for episode in range(episodes):
        # Reset the game environment before each episode
        game = BlackjackGame()
        game.reset()

        # Randomly sample a row from the dataset
        sample = data.sample(n=1).iloc[0]
        
        # Extract relevant features from the sample
        player_sum = sample['sumofcards']
        dealer_sum = sample['sumofdeal']
        game_outcome = sample['winloss']  # Can also use 'plybustbeat' and 'dlbustbeat'
        
        # Initialize the state (current game state)
        state = (player_sum, dealer_sum)
        
        # Choose an action using Q-learning agent
        action = q_learning_agent.get_best_action(state)
        
        # Perform the action and simulate the result
        game.step(action)
        
        # Get the next state after taking the action
        next_state = (game.player_total, game.dealer_total)
        
        # Reward based on the outcome
        if game_outcome == 1:  # Player wins
            reward = 1
        elif game_outcome == -1:  # Dealer wins
            reward = -1
        else:  # Tie
            reward = 0
        
        # Update Q-values using the Q-learning update rule
        q_learning_agent.update_q_values(state, action, reward, next_state)
    
    return q_learning_agent

# Load the dataset
data = pd.read_csv('data/blkjckhands.csv')

# Train the Q-learning agent
trained_agent = train_agent(data)

# Example of how to use the trained agent to predict the next move
# Sample state (e.g., player sum: 15, dealer sum: 10)
state = (15, 10)
action = trained_agent.get_best_action(state)
print(f"Recommended action: {action}")
