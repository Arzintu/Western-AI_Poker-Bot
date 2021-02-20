import random
from termcolor import colored

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


class Deck:

    def __init__(self):

        # Deck properties
        self.card = [0]*52
        self.size = 52
        self.top = -1

        # Deck Card Index
        index = 0

        # Create Deck
        for suit in range(1,5):
            for value in range(2,15):
                self.card[index] = Card(suit, value)
                index += 1

        # Shuffle Deck
        random.shuffle(self.card)

    # Draw card from top of the deck
    def draw(self):
        # Utilize Pick function
        return self.pick(self.top)

    # Deal hand
    def deal(self):
        card_1 = self.pick(self.top)
        card_2 = self.pick(self.top)
        return [card_1, card_2]

    # Pick a card from the deck at a specified location
    def pick(self, value):
        try:
            card = self.card[value]
            self.top -= 1
            return card

        except IndexError:
            print("Pick a card inside the bounds 0 - " + self.size)

    # Reset deck by returning played cards to the deck and reshuffle
    def reset(self):
        # Reset index to top of deck
        self.top = -1
        # Reshuffle deck
        random.shuffle(self.card)

    # Size of deck
    def get_size(self):
        return 52 + self.top + 1


class Player:
    def __init__(self, deck, name):
        self.name = name
        self.card = deck.deal()

    # Get Functions
    def get_name(self):
        return self.name

    def get_hand(self):
        return self.card

    def get_hand_info(self):
        return [self.card[0].get_info(), self.card[1].get_info()]

    # Set Function
    def set_name(self, name):
        self.name = name


class Game:
    def __init__(self, number_of_players):

        # Game Class variables
        self.deck = Deck()
        self.number_of_players = number_of_players

        self.player = [0] * self.number_of_players
        self.player_card = [0] * self.number_of_players * 2
        self.game_card = [0] * 5

        # Instantly start a new game
        self.play()

    # Play a game of Poker
    def play(self):
        self.deck.reset()

        # Draw Player Cards
        for p in range(self.number_of_players):
            self.player[p] = Player(self.deck, p)

            # Need to determine format
            # Store cards in array
            self.player_card[p] = self.player[p].card[0].get_info()
            self.player_card[p+1] = self.player[p].card[1].get_info()

        # Draw Game Cards
        for x in range(5):
            # Store cards in array
            self.game_card[x] = self.deck.draw()

    # Get Functions
    def get_players(self):
        return self.player

    def get_player_cards(self):
        return self.player_card

    def get_game_cards(self):
        return self.game_card

    # Placeholder Code
    def game_state(self):
        return self.game_card, self.player_card

    # Set Function
    def set_number_of_players(self, number_of_players):
        self.number_of_players = number_of_players


# class Hand_Classifciation:
    # def __init__(self, Game):


color_map = {1: "red", 2: "red", 3: "white", 4: "white"}
suit_map = {1: "\u2764", 2: "\u2666", 3: "\u2660", 4: "\u2663"}
number_map = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10',  11: 'J', 12: 'Q', 13: 'K', 14: 'A'}


poker = Game(2)
for game in range(100):
    poker.play()

    print("Game " + str(game))
    for player in poker.get_players():
        player_cards = player.get_hand()

        print("Player " + str(player.get_name()))

        for card in player_cards:
            string_color = color_map[card.get_suit()]
            string_card = suit_map[card.get_suit()] + " " + number_map[card.get_value()]
            print(colored(string_card, string_color), end=" ")
        print()

    print("Game Cards")
    for card in poker.get_game_cards():
        string_color = color_map[card.get_suit()]
        string_card = suit_map[card.get_suit()] + " " + number_map[card.get_value()]
        print(colored(string_card, string_color), end="  ")
    print()
    print()

