
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # Get Functions
    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value

    def get_info(self):
        return self.suit, self.value

    # Set Functions
    def set_suit(self, suit):
        self.suit = suit

    def set_value(self, value):
        self.value = value
