from collections import Counter


class EvaluateHand:

    def __init__(self, game, player):

        self.card = list(game.get_cards())
        self.card.extend(player.get_hand())
        self.player_hand = player.get_hand()

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
        self.score = [0]*10

        self.count()

    def count(self):

        # Card Sort Structure

        #    1 2 3 4 5 5 6 7 8 9 10 J Q K A
        # H  X     X
        # D      X X X
        # S                  X   X
        # C

        card_sort = [[0 for i in range(4)] for j in range(13)]
        # https://www.adda52.com/poker/poker-rules/cash-game-rules/tie-breaker-rules#:~:text=The%20highest%20pair%20is%20used,used%20to%20break%20the%20tie.&text=Remaining%203-,If%20two%20or%20more%20players%20hold,pair%20then%20highest%20pair%20wins.
        for card in self.card:
            card_sort[card.get_value()-2][card.get_suit()] = 1

        sequence_count = 0
        track_suit = [0, 0, 0, 0]
        for rank in range(2, 15):

            rank_count = 0
            for suit in range(4):
                if card_sort[rank-2][suit]:
                    rank_count += 1
                    track_suit[suit] += 1
                else:
                    track_suit[suit] = 0

            if rank_count:

                sequence_count += 1

                # High Card
                if rank_count == 1:
                    self.high_card = rank
                    self.score[0] = rank

                # Pair
                # Two Pair
                if rank_count == 2:
                    # Two Pair
                    if self.pair != 0:
                        self.two_pair = max(self.pair, rank)
                        self.pair = min(self.pair, rank)

                        self.score[2] = self.two_pair
                        self.score[1] = self.pair

                    # Pair
                    else:
                        self.pair = rank
                        self.score[1] = self.pair

                # Three of a Kind
                elif rank_count == 3:
                    self.three_of_a_kind = rank
                    self.score[3] = rank

                # Four of a Kind
                elif rank_count == 4:
                    self.four_of_a_kind = rank
                    self.score[7] = rank

                # Straight
                # Straight Flush
                # Royal Flush
                if sequence_count == 5:

                    self.straight = rank
                    self.score[4] = rank

                    for suit in track_suit:
                        if suit == 5:

                            if rank != 14:
                                self.straight_flush = rank
                                self.score[8] = self.straight_flush
                                print("Straight Flush!")

                            else:
                                self.royal_flush = rank
                                self.score[9] = self.royal_flush
                                print("Royal!")

            # No card of specified rank counted
            else:
                # Reset Straight Count
                sequence_count = 0

        # Full House
        if self.pair != 0 and self.three_of_a_kind != 0:
            self.full_house = self.three_of_a_kind * 13 + self.pair
            self.score[6] = self.full_house

        # print("Evaluated: [H, 2K, 2P, 3K, ST, FL, FH, 4K, SF, RF")
        # print("Evaluated: ", end="")
        print(self.score)




    def eval_two_kind(self):
        c = Counter(c.value for c in self.card)

        return False

    def print(self):
        print("Player Hand Info")
        print("High Card: " + str(self.high_card))
        print("Pair: " + str(self.high_card))
