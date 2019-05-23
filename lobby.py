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
        self.game_pot = 0

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

    def init_lobby(self, chips=0):
        for player in self.players:
            player.init_player(chips)

    def start_game(self):
        self.num_games += 1
        print("Hand number: " + str(self.num_games))
        self.play_rounds()

    def play_rounds(self):
        while self.num_rounds < 5 and len(self.players) > 0:
            if len(self.players) == 1:
                print("You are the winner " + self.players[0].name + "!")
                break
            if self.num_rounds == 1:
                print("Pre-Flop")
                self.hand_out_cards()
                self.num_rounds += 1
                self.player_action()
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

    def determine_winner(self):
        winner = self.players[0].name
        print("You are the winner " + str(winner) + "!")

    def hand_out_cards(self):
        cards_to_deal = 2
        for i in range(cards_to_deal):
            for player in self.players:
                player.add_card(self.deck.cards.pop())

    def player_action(self):
        current_bet = 0
        for player in self.players:
            has_player_done_action = False
            was_their_a_bet = False
            was_their_a_raise = False
            current_player_list = []

            while not has_player_done_action:
                if not getattr(player, "user"):  # allows players to fold or check
                    action = input(getattr(player, "name") + ", what would you like to do?: ")

                    if action == "Check" or action == "check":  # check
                        has_player_done_action = True
                        current_player_list.append(player)
                        pass

                    if action == "Fold" or action == "fold":  # fold
                        self.players.remove(player)
                        has_player_done_action = True

                    if action == "Bet" or action == "bet":  # bet
                        bet = input("How much do you want to bet?: ")
                        if getattr(player, "chip_value") - int(bet) > 0:
                            current_bet = int(bet)
                            self.game_pot += int(bet)  # adds the bet to the pot
                            setattr(player, "chip_value", getattr(player, "chip_value") - int(bet))  # removes the bet from the chip count of the player
                            print(str(bet) + " was bet!")
                            print("Pot is currently: " + str(self.game_pot))
                            has_player_done_action = True
                            was_their_a_bet = True
                        else:
                            print("You do not have enough chips!")

                    if action == "Call" or action == "call":
                        if current_bet > 0:
                            if not (getattr(player, "chip_value") - current_bet) < 0:
                                self.game_pot += current_bet
                                setattr(player, "chip_value", getattr(player, "chip_value") - current_bet)
                                has_player_done_action = True
                            else:
                                print("You do not have enough chips!")
                                all_in = input("Would you like to go all in? ")
                                if all_in == "Yes" or all_in == "yes":
                                    self.game_pot += getattr(player, "chip_value")
                                    setattr(player, "chip_value", 0)
                                    has_player_done_action = True
                                else:
                                    self.players.remove(player)
        return self.players
