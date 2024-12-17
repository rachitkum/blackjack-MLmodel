# game/blackjack_game.py
import random

class BlackjackGame:
    def __init__(self):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
        self.player_hand = []
        self.dealer_hand = []

    def reset(self):
        """Reset the game for a new round."""
        random.shuffle(self.deck)
        self.player_hand = [self.deck.pop(), self.deck.pop()]
        self.dealer_hand = [self.deck.pop(), self.deck.pop()]

    def step(self, action):
        """Take an action: 'hit' or 'stand'."""
        if action == 'hit':
            self.player_hand.append(self.deck.pop())
        elif action == 'stand':
            while sum(self.dealer_hand) < 17:
                self.dealer_hand.append(self.deck.pop())

    @property
    def player_total(self):
        return sum(self.player_hand)

    @property
    def dealer_total(self):
        return sum(self.dealer_hand)

    def result(self):
        """Determine the outcome of the game."""
        if self.player_total > 21:
            return "You Bust! Dealer Wins!"
        elif self.dealer_total > 21 or self.player_total > self.dealer_total:
            return "You Win!"
        elif self.player_total == self.dealer_total:
            return "It's a Tie!"
        else:
            return "Dealer Wins!"
