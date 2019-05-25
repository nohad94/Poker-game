from deck import *


class Game:
    def __init__(self, list_of_players):
        self.player_list = list_of_players
        self.deck = Deck()
        self.pot = 0
        self.board = []
        self.num_rounds = 1

    def hand_out_cards(self):
        cards_to_deal = 2
        for i in range(cards_to_deal):
            for player in self.player_list:
                player.add_card(self.deck.cards.pop())

    def deal_flop(self):
        self.deck.cards.pop()
        card1 = self.deck.cards.pop()
        self.board.append(card1)
        card2 = self.deck.cards.pop()
        self.board.append(card2)
        card3 = self.deck.cards.pop()
        self.board.append(card3)

    def deal_turn(self):
        self.deck.cards.pop()
        card1 = self.deck.cards.pop()
        self.board.append(card1)

    def deal_river(self):
        self.deck.cards.pop()
        card1 = self.deck.cards.pop()
        self.board.append(card1)

    def play_rounds(self):
        while self.num_rounds < 5 and len(self.player_list) > 0:
            play_round = Round(self.player_list, self.pot)
            if len(self.player_list) == 1:
                print("You are the winner " + self.player_list[0].name + "!")
                break
            if self.num_rounds == 1:
                print("Pre-Flop")
                print(self.board)
                self.hand_out_cards()
                self.num_rounds += 1
                self.pot = Round.player_actions(play_round, self.player_list)
            if self.num_rounds == 2:
                self.deal_flop()
                print("Flop")
                print(self.board)
                self.num_rounds += 1
                self.pot = Round.player_actions(play_round, self.player_list)
            if self.num_rounds == 3:
                self.deal_turn()
                print("Turn")
                print(self.board)
                self.num_rounds += 1
                self.pot = Round.player_actions(play_round, self.player_list)
            if self.num_rounds == 4:
                self.deal_river()
                print("River")
                print(self.board)
                self.pot = Round.player_actions(play_round, self.player_list)
                break


class Round:
    def __init__(self, list_of_players, pot):
        self.list_of_players = list_of_players
        self.round_over = False
        self.current_bet = 0
        self.pot = pot

    def player_actions(self, list1):
        for person in list1:
            action = input(person.get_name() + " What is your action? ")

            if action == "Check" or action == "check":
                self.check()
            if action == "Bet" or action == "bet":
                self.bet()
            if action == "Raise" or action == "raise":
                self.raise_bet()
            if action == "Call" or action == "call":
                self.call()
            if action == "Fold" or action == "fold":
                self.fold()
        return self.pot

    def check(self):
        if self.current_bet > 0:
            cannot_check = input("You cannot check, please pick another action ")
            if cannot_check == "Call" or cannot_check == "call":
                self.call()
            if cannot_check == "Fold" or cannot_check == "fold":
                self.fold()
            if cannot_check == "Raise" or cannot_check == "raise":
                self.raise_bet()
            if cannot_check == "Check" or cannot_check == "check":
                self.check()
            if cannot_check == "Bet" or cannot_check == "bet":
                self.bet()
        else:
            self.list_of_players = self.list_of_players[1:] + [(self.list_of_players[0])]
            pass

    def fold(self):
        self.list_of_players.remove(self)

    def call(self):
        if (getattr(self, "chip_value") - self.current_bet) >= 0:
            self.pot += self.current_bet
            setattr(self, "chip_value", getattr(self, "chip_value") - self.current_bet)
            self.list_of_players = self.list_of_players[1:] + [(self.list_of_players[0])]
            setattr(self, "put_in_pot", self.current_bet)
        else:
            cannot_call = input("You cannot call, please pick another action ")
            if cannot_call == "Call" or cannot_call == "call":
                self.call()
            if cannot_call == "Fold" or cannot_call == "fold":
                self.fold()
            if cannot_call == "Raise" or cannot_call == "raise":
                self.raise_bet()
            if cannot_call == "Check" or cannot_call == "check":
                self.check()
            if cannot_call == "Bet" or cannot_call == "bet":
                self.bet()

    def bet(self):
        if self.current_bet > 0:
            what_next = input("You must raise, call or fold. You cannot bet!")
            if what_next == "Call" or what_next == "call":
                self.call()
            if what_next == "Fold" or what_next == "fold":
                self.fold()
            if what_next == "Raise" or what_next == "raise":
                self.raise_bet()
            if what_next == "Check" or what_next == "check":
                self.check()
            if what_next == "Bet" or what_next == "bet":
                self.bet()
        else:
            your_bet = int(input("How much do you want to bet? "))
            if your_bet > getattr(self, "chip_value"):
                cannot_bet = input("You do not have enough chips to make that bet! please choose another action")
                if cannot_bet == "Bet" or cannot_bet == "bet":
                    self.bet()
                if cannot_bet == "Call" or cannot_bet == "call":
                    self.call()
                if cannot_bet == "Fold" or cannot_bet == "fold":
                    self.fold()
                if cannot_bet == "Raise" or cannot_bet == "raise":
                    self.raise_bet()
                if cannot_bet == "Check" or cannot_bet == "check":
                    self.check()
            else:
                self.current_bet = your_bet
                self.pot += your_bet
                setattr(self, "chip_value", (getattr(self, "chip_value") - your_bet))
                self.list_of_players = self.list_of_players[1:] + [(self.list_of_players[0])]

    def raise_bet(self):
        your_raise = int(input("What is your raise? "))
        if self.current_bet == 0 or self.current_bet*2 > your_raise or your_raise > getattr(self, "chip_value"):
            cannot_raise = input("You cannot raise that amount! Choose another function ")
            if cannot_raise == "Bet" or cannot_raise == "bet":
                self.bet()
            if cannot_raise == "Call" or cannot_raise == "call":
                self.call()
            if cannot_raise == "Fold" or cannot_raise == "fold":
                self.fold()
            if cannot_raise == "Raise" or cannot_raise == "raise":
                self.raise_bet()
            if cannot_raise == "Check" or cannot_raise == "check":
                self.check()
        else:
            self.current_bet = your_raise
            self.pot += your_raise
            setattr(self, "chip_value", getattr(self, "chip_value") - your_raise)
            self.list_of_players = self.list_of_players[1:] + [(self.list_of_players[0])]
