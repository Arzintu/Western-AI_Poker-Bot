from Card import Card
import random

class Deck:

    def __init__(self):

        # Deck properties
        self.card = [0]*52
        self.size = 52
        self.top = 0

        # Deck Card Index
        index = 0

        # Create Deck
        for suit in range(0,4):
            for value in range(2,15):
                self.card[index] = Card(suit, value)
                index += 1

        # Shuffle Deck
        random.shuffle(self.card)

    # Draw card from top of the deck
    def draw(self):
        # Utilize Pick function
        self.top += 1
        return self.pick(self.top)

    # Deal hand
    def deal(self):
        card_1 = self.draw()
        card_2 = self.draw()
        return [card_1, card_2]

    # Pick a card from the deck at a specified location
    def pick(self, value):
        try:
            card = self.card[value]
            return card

        except IndexError:
            print("Pick a card inside the bounds 0 - " + self.size)

    # Reset deck by returning played cards to the deck and reshuffle
    def reset(self):
        # Reset index to top of deck
        self.top = 0
        # Reshuffle deck
        random.shuffle(self.card)

    # Size of deck
    def get_size(self):
        return 52 - self.top
