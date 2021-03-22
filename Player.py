class Player:
    def __init__(self, deck, name):
        self.name = name

        # [card_1, card_2]
        self.card = deck.deal()
        self.score = [2, 10]

    # Get Functions
    def get_name(self):
        return self.name

    def get_cards(self):
        self.get_hand()

    def get_hand(self):
        return self.card

    def get_hand_info(self):
        return [self.card[0].get_info(), self.card[1].get_info()]

    def get_score(self):
        return self.score

    # Set Function
    def set_name(self, name):
        self.name = name

    def set_score(self, score):
        self.score = score
