
class Card:
    def __init__(self, value, house):
        self.value = value
        self.house = house

    def __repr__(self):
        return f"{self.value}{self.house}"



