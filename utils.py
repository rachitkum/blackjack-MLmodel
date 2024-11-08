from game_logic import card_values

# Adjusts for aces if the hand exceeds 21
def adjust_for_aces(hand):
    total = sum(card_values[card] for card in hand)
    aces = hand.count("A")
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total
