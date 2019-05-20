import random
from random import shuffle

from player import *
from deck import *


class Lobby:
    LIST_NAME = ["Jim", "Kevin", "Pam", "Michael", "Dwight", "Creed", "Toby", "Oscar", "Meredith", "Stanley", "Angela"]
    STATES = ["Beginning", "In Round", "End round"]

    def __init__(self, num_players, num_bots):
        self.players = self.generate_players(num_players, num_bots)
        self.dealer = random.randint(0, 8)
        self.deck = Deck()
        self.discarded = []
        self.state = "Beginning"

    def generate_players(self, num_players, num_bots):
        player_list = []
        for i in range(int(num_bots)):
            player_list.append(Player(random.choice(self.LIST_NAME), 0, True, False))
        for i in range(int(num_players)):
            user_name_choice = input("Choose a name: ")
            player_list.append(Player(user_name_choice, 0, False, False))
        shuffle(player_list)
        return player_list

    def move_dealer(self):
        self.players[self.dealer].set_dealer(False)
        self.dealer = (self.dealer + 1) % len(self.players)
        self.players[self.dealer].set_dealer(True)

    def __repr__(self):
        return str({"players": self.players, "dealer": self.dealer, "deck": self.deck})

    def init_lobby(self, chips=5000):
        for player in self.players:
            player.init_player(chips)

    def start_round(self):
        self.hand_out_cards()

    def hand_out_cards(self):
        cards_to_deal = 2

        for i in range(cards_to_deal):
            for player in self.players:
                player.add_card(self.deck.cards.pop())


