import random
from player import *
from game import *


class Lobby:
    LIST_NAME = ["Jim", "Kevin", "Pam", "Michael", "Dwight", "Creed", "Toby", "Oscar", "Meredith", "Stanley", "Angela"]
    STATES = ["Beginning", "In Round", "End round"]

    def __init__(self, num_players, num_bots):
        self.players = self.generate_players(num_players, num_bots)

    def generate_players(self, num_players, num_bots):
        player_list = []
        for i in range(int(num_bots)):
            player_list.append(Player(random.choice(self.LIST_NAME), 0, True, 0))
        for i in range(int(num_players)):
            user_name_choice = input("Choose a name: ")
            player_list.append(Player(user_name_choice, 0, False, 0))
        shuffle(player_list)
        return player_list

    def __repr__(self):
        return str({"players": self.players})

    def init_lobby(self, chips=0):
        for player in self.players:
            player.init_player(chips)

    def start_game(self):
        while len(self.players) > 1:
            game = Game(self.players)
            game.play_rounds()
