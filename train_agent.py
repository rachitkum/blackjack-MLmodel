# train_agent.py
import pandas as pd
from q_learning.q_learning import QLearningAgent
from game.blackjack_game import BlackjackGame

def train_agent(data, episodes=2000):
    agent = QLearningAgent()

    for episode in range(episodes):
        game = BlackjackGame()
        game.reset()

        sample = data.sample(n=1).iloc[0]
        player_sum = sample['sumofcards']
        dealer_card = sample['dealcard1']
        outcome = sample['winloss']

        state = (player_sum, dealer_card)
        action = agent.get_best_action(state)

        game.step(action)
        next_state = (game.player_total, game.dealer_hand[0])

        if outcome == 'Win':
            reward = 1
        elif outcome == 'Loss':
            reward = -1
        else:
            reward = 0

        agent.update_q_values(state, action, reward, next_state)

    agent.save('saved_models/q_learning_agent.pkl')

if __name__ == "__main__":
    dataset = pd.read_csv('data/blkjckhands.csv')
    train_agent(dataset, episodes=2000)
