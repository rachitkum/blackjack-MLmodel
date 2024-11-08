import random

class BlackjackGame:
    def __init__(self):
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []
        self.player_total = 0
        self.dealer_total = 0

    def create_deck(self):
        """Creates a deck of cards (each card is an integer value from 1 to 11)."""
        deck = [i for i in range(1, 12)] * 4  # 4 decks of cards (simplified)
        random.shuffle(deck)
        return deck

    def reset(self):
        """Resets the game to the initial state."""
        self.deck = self.create_deck()
        self.player_hand = [self.deck.pop(), self.deck.pop()]
        self.dealer_hand = [self.deck.pop(), self.deck.pop()]
        self.player_total = sum(self.player_hand)
        self.dealer_total = sum(self.dealer_hand)

    def step(self, action):
        """Executes the action ('hit' or 'stand')"""
        if action == 'hit':
            self.player_hand.append(self.deck.pop())
            self.player_total = sum(self.player_hand)
        elif action == 'stand':
            while self.dealer_total < 17:
                self.dealer_hand.append(self.deck.pop())
                self.dealer_total = sum(self.dealer_hand)
        else:
            raise ValueError("Action must be 'hit' or 'stand'.")

    def get_state(self):
        """Returns the current state of the game."""
        return (self.player_total, self.dealer_total)

    def get_result(self):
        """Returns the result of the game (-1: dealer wins, 1: player wins, 0: tie)."""
        if self.player_total > 21:
            return -1  # Player busts
        if self.dealer_total > 21:
            return 1  # Dealer busts
        if self.player_total > self.dealer_total:
            return 1  # Player wins
        elif self.player_total < self.dealer_total:
            return -1  # Dealer wins
        else:
            return 0  # Tie
