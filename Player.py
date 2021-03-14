class Player:
    def __init__(self, deck, name):
        self.name = name
        self.card = deck.deal()

    # Get Functions
    def get_name(self):
        return self.name

    def get_cards(self):
        self.get_hand()

    def get_hand(self):
        return self.card

    def get_hand_info(self):
        return [self.card[0].get_info(), self.card[1].get_info()]

    # Set Function
    def set_name(self, name):
        self.name = name
