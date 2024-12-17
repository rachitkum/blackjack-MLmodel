# main.py
from q_learning.q_learning import QLearningAgent
from game.blackjack_game import BlackjackGame

def main():
    agent = QLearningAgent.load('saved_models/q_learning_agent.pkl')

    while True:
        game = BlackjackGame()
        game.reset()

        print("--- New Round ---")
        while True:
            print(f"Dealer's Visible Card: {game.dealer_hand[0]}")
            print(f"Your Hand: {game.player_hand} | Total: {game.player_total}")

            state = (game.player_total, game.dealer_hand[0])
            suggestion = agent.get_best_action(state)
            print(f"Suggested Action: {suggestion}")

            action = input("Choose 'hit' or 'stand' (or 'quit' to exit): ").strip().lower()
            if action == 'quit':
                print("Thanks for playing!")
                return

            game.step(action)

            if game.player_total > 21 or action == 'stand':
                break

        print(f"Your Hand: {game.player_hand} | Total: {game.player_total}")
        print(f"Dealer's Final Hand: {game.dealer_hand} | Total: {game.dealer_total}")
        print(f"Outcome: {game.result()}\n")

if __name__ == "__main__":
    main()
