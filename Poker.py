from Deck import Deck
from Player import Player
from Evaluate_Hand import EvaluateHand
from termcolor import colored

from openpyxl import Workbook


class Game:

    filename = "C:/Users/Owner/Documents/GitHub/Western-AI_Poker-Bot/Poker_Data.xlsx"
    wb = Workbook(write_only=True)
    ws = wb.create_sheet()

    def __init__(self, number_of_players):

        # Game Class variables
        self.deck = Deck()
        self.number_of_players = number_of_players

        self.player = [0] * self.number_of_players
        self.card = [0] * 5

        # Review variable
        # self.player_card = [0] * self.number_of_players * 2

        # Instantly start a new game
        self.excel_header()
        self.play()

    # Simulate x number of poker games
    def simulate(self, number_of_games):

        # Simulate poker games
        for n in range(number_of_games):
            if n % 10000 == 0:
                print("Game " + str(n + 1))
            self.play()

            # Evaluate each player's hand
            for player in self.player:
                evaluate = EvaluateHand(self, player)
                hand_assignment = evaluate.count()

            # Export Data to Excel
            self.ws.append(self.extract_game_data(hand_assignment, n))

        # Save Excel File
        self.wb.save(r"C:/Users/Owner/Documents/GitHub/Western-AI_Poker-Bot/Poker_Data.xlsx")

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

    def extract_game_data(self, hand_assignment, n):

        p_list = []
        b_list = []

        for p in range(self.number_of_players):
            for card in self.player[p].get_hand():
                p_list.append(card.get_suit())
                p_list.append(card.get_value())

        for card in self.card:
            b_list.append(card.get_suit())
            b_list.append(card.get_value())

        p_list.extend(b_list)
        p_list.extend([hand_assignment])
        return (p_list)

    def excel_header(self):
        headers = ['Card 1 suit', 'Card 1 value', 'Card 2 suit', 'Card 2 value', 'Card 3 suit', 'Card 3 value',
                   'Card 4 suit',
                   'Card 4 value', 'Card 5 suit', 'Card 5 value', 'Card 6 suit', 'Card 6 value', 'Card 7 suit',
                   'Card 7 value',
                   'Label']

        self.ws.append(headers)

    def save_excel_file(self):
        self.wb.save()

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


        print("Game Cards")
        for card in self.get_cards():
            string_color = color_map[card.get_suit()]
            string_card = suit_map[card.get_suit()] + " " + number_map[card.get_value()]
            print(colored(string_card, string_color), end="  ")
        print()
        print()

poker = Game(1)
num_games = 5000000

poker.simulate(num_games)


