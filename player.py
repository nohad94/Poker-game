class Player:
    def __init__(self, name, chip_value, user, put_in_pot):
        self.name = name
        self.chip_value = chip_value
        self.user = user  # bot = True, player = False.
        self.cards = []
        self.put_in_pot = 0

    def get_name(self):
        return self.name

    def get_chip_value(self):
        return self.get_chip_value

    def get_user(self):
        return self.user

    def get_put_in_pot(self):
        return self.put_in_pot

    def set_put_in_pot(self, value):
        setattr(self, "put_in_pot", value)

    def init_player(self, chips):
        self.chip_value = chips

    def add_card(self, card):
        self.cards.append(card)

    def __str__(self):
        return self.name

    def __repr__(self):
        return str({"name": self.name, "chip": self.chip_value, "cards": self.cards})
