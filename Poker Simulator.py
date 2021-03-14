from collections import Counter
from operator import itemgetter
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
        self.top = 0

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

            # Delete storing data twice
            # Need to determine format
            # Store cards in array
            # self.player_card[p] = self.player[p].card[0].get_info()
            # self.player_card[p+1] = self.player[p].card[1].get_info()

        # Draw Game Cards
        for x in range(5):
            # Store cards in array
            self.card[x] = self.deck.draw()

        hand = Hand_Classifciation(self)

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
        color_map = {1: "red", 2: "red", 3: "white", 4: "white"}
        suit_map = {1: "\u2764", 2: "\u2666", 3: "\u2660", 4: "\u2663"}
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


class Hand_Classifciation:
    def __init__(self, game):

        self.card = list(game.get_cards())
        self.card.extend(game.player[0].get_hand())
        self.player_hand = game.player[0].get_hand()

        """""
        self.player_card = [0] * self.number_of_players * 2
        self.game_card = [0] * 5
        """""

        self.high_card = 0
        self.pair = 0
        self.two_pair = 0
        self.three_of_a_kind = 0
        self.straight = 0
        self.flush = 0
        self.full_house = 0
        self.four_of_a_kind = 0
        self.straight_flush = 0
        self.royal_flush = 0

        self.count()

    def count(self):

        # Card Sort Structure

        #    1 2 3 4 5 5 6 7 8 9 10 J Q K A
        # H  X     X
        # D      X X X
        # S                  X   X
        # C

        card_sort = [[0, 0, 0, 0]] * 13
        # https://www.adda52.com/poker/poker-rules/cash-game-rules/tie-breaker-rules#:~:text=The%20highest%20pair%20is%20used,used%20to%20break%20the%20tie.&text=Remaining%203-,If%20two%20or%20more%20players%20hold,pair%20then%20highest%20pair%20wins.
        for card in self.card:

            card_sort[card.get_value()-2][card.get_suit()] = 1

        sequence_count = 0
        track_suit = [0, 0, 0, 0]
        for rank in range(len(card_sort)):

            rank_count = 0
            for suit in range(0, 5):
                if suit:
                    rank_count += 1
                    track_suit[suit] += 1
                else:
                    track_suit[suit] = 0

            if rank_count:

                sequence_count += 1

                # High Card
                if rank_count == 1:
                    self.high_card = rank

                # Pair
                # Two Pair
                if rank_count == 2:
                    # Two Pair
                    if self.pair != 0:
                        self.two_pair = max(self.pair, rank)
                        self.pair = min(self.par, rank)

                    # Pair
                    else:
                        self.pair = rank

                # Three of a Kind
                elif rank_count == 3:
                    self.three_of_a_kind = rank

                # Four of a Kind
                elif rank_count == 4:
                    self.four_of_a_kind = rank

                # Straight
                # Straight Flush
                # Royal Flush
                if sequence_count == 5:
                    self.straight = rank

                    for suit in track_suit:
                        if suit == 5:
                            self.straight_flush = rank
                            if rank == 13:
                                self.royal_flush = rank

            # No card of specified rank counted
            else:
                # Reset Straight Count
                sequence_count = 0

        # Full House
        if self.pair != 0 and self.three_of_a_kind != 0:
            self.full_house = self.three_of_a_kind * 13 + self.pair




    def eval_high_card(self):
        self.high_card = max(self.player_hand, key=itemgetter(1))[0]

    def eval_two_kind(self):
        c = Counter(c.value for c in self.card)

        return False

    def print(self):
        print("Player Hand Info")
        print("High Card: " + str(self.high_card))
        print("Pair: " + str(self.high_card))

poker = Game(2)
poker.simulate(100)


