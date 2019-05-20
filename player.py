class Player:
    def __init__(self, name, chip_value, user, dealer):
        self.name = name
        self.chip_value = chip_value
        self.user = user  # bot = True, player = False.
        self.dealer = dealer  # if true, they are in the dealer position, if false they are not.
        self.cards = []

    def get_name(self):
        return self.name

    def get_chip_value(self):
        return self.get_chip_value

    def get_user(self):
        return self.user

    def get_dealer(self):
        return self.dealer

    def set_dealer(self, value):
        return self.dealer

    def init_player(self, chips):
        self.chip_value = chips

    def add_card(self, card):
        self.cards.append(card)

    def __str__(self):
        return self.name

    def __repr__(self):
        return str({"name": self.name, "chip": self.chip_value, "cards": self.cards})


# def player_action():
#     round_list = lst
#     print(round_list)
#
#     for player in round_list:
#         player_split = player.split()
#         print(player_split)
#         if player_split[2] == "False":  # allows players to fold or check
#             action = input("What would you like to do?: ")
#             if action == "Check":
#                 pass
#             if action == "Fold":
#                 round_list.remove(player)
#                 # bots always check
#     return round_list
