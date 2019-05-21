import random
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
        self.num_rounds = 1
        self.num_games = 0

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

    def init_lobby(self, chips=int(input("Starting Chips: "))):
        for player in self.players:
            player.init_player(chips)

    def start_game(self):
        self.num_games += 1
        print("Hand number: " + str(self.num_games))
        self.play_rounds()

    def play_rounds(self):
        self.start_round()
        while self.num_rounds < 5 and len(self.players) > 0:
            if len(self.players) == 1:
                print("You are the winner " + self.players[0].name + "!")
                break
            if self.num_rounds == 2:
                print("Flop")
                self.num_rounds += 1
                self.player_action()
            if self.num_rounds == 3:
                print("Turn")
                self.num_rounds += 1
                self.player_action()
            if self.num_rounds == 4:
                print("River")
                self.player_action()
                self.determine_winner()
                break

    def start_round(self):
        print("Pre-Flop")
        self.hand_out_cards()
        self.num_rounds += 1
        self.player_action()

    def determine_winner(self):
        winner = self.players[0].name
        print("You are the winner " + str(winner) + "!")

    def hand_out_cards(self):
        cards_to_deal = 2
        for i in range(cards_to_deal):
            for player in self.players:
                player.add_card(self.deck.cards.pop())

    def player_action(self):
        for player in self.players:
            if not getattr(player, "user"):  # allows players to fold or check
                action = input(getattr(player, "name") + ", what would you like to do?: ")
                if action == "Check":
                    pass
                if action == "Fold":
                    self.players.remove(player)
                    # bots always check
        return self.players



