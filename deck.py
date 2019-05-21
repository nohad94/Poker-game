
from random import shuffle
from card import *


class Deck:
    ALLOWED_VALUES = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
    ALLOWED_HOUSES = ("♥", "♦", "♣", "♠")

    def __init__(self):
        self.cards = self.generate_cards()

    def generate_cards(self):
        deck = []
        for house in self.ALLOWED_HOUSES:
            for value in self.ALLOWED_VALUES:
                card = Card(value, house)
                deck.append(card)
        shuffle(deck)
        return deck

    def __repr__(self):
        return str({"cards": self.cards})
