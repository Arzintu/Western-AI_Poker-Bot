from Deck import Deck
from Player import Player
from Evaluate_Hand import EvaluateHand
from termcolor import colored


class Game:
    def __init__(self, number_of_players):

        # Game Class variables
        self.deck = Deck()
        self.number_of_players = number_of_players

        self.player = [0] * self.number_of_players
        self.card = [0] * 5

        # Review variable
        # self.player_card = [0] * self.number_of_players * 2

        # Instantly start a new game
        self.play()

    # Simulate x number of poker games
    def simulate(self, number_of_games):
        for n in range(number_of_games):
            print("Game " + str(n + 1))
            self.play()
            self.print()

    # Play a game of Poker
    def play(self):
        self.deck.reset()

        # Draw Player Cards
        for p in range(self.number_of_players):
            self.player[p] = Player(self.deck, p)

        # Draw Game Cards
        for x in range(5):
            # Store cards in array
            self.card[x] = self.deck.draw()


    def game_to_excel(self, n):

        plist = []
        glist = []
        for player in self.player:
            for card in self.player.get_hand():
                plist.append(card.getsuit())
                plist.append(card.get_vale())
                plist.extend(player.get_score())

        for card in self.card:
            glist.append(card.getsuit())
            glist.apend(card.get_vale)

        rlist = glist.extend(plist)

        # Row to excel using openpyxl

    # Get Functions
    def get_players(self):
        return self.player

    def get_cards(self):
        return self.card

    # Placeholder Code
    def game_state(self):
        return self.card, self.card

    # Set Function
    def set_number_of_players(self, number_of_players):
        self.number_of_players = number_of_players

    def print(self):
        color_map = {0: "red", 1: "red", 2: "white", 3: "white"}
        suit_map = {0: "\u2764", 1: "\u2666", 2: "\u2660", 3: "\u2663"}
        number_map = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q',
                      13: 'K', 14: 'A'}

        for player in self.get_players():
            player_cards = player.get_hand()

            print("Player " + str(player.get_name()))

            for card in player_cards:
                string_color = color_map[card.get_suit()]
                string_card = suit_map[card.get_suit()] + " " + number_map[card.get_value()]
                print(colored(string_card, string_color), end=" ")


            print()
            EvaluateHand(self, player)

        print("Game Cards")
        for card in self.get_cards():
            string_color = color_map[card.get_suit()]
            string_card = suit_map[card.get_suit()] + " " + number_map[card.get_value()]
            print(colored(string_card, string_color), end="  ")
        print()
        print()

poker = Game(2)
poker.simulate(1000)