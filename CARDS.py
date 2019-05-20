import random


def generate_deck():
    final = []
    list1 = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

    for a in list1:
        final.append(str(a) + "♥")
    for a in list1:
        final.append(str(a) + "♦")
    for a in list1:
        final.append(str(a) + "♣")
    for a in list1:
        final.append(str(a) + "♠")
    return final


def give_card(lst):
    list_of_cards = generate_deck()
    final_player = []
    for i in lst:
        card1 = random.choice(list_of_cards)
        card2 = random.choice(list_of_cards)
        i = str(i) + " [" + card1 + "]" + "[" + card2 + "]"
        list_of_cards.remove(card1)
        list_of_cards.remove(card2)
        final_player.append(i)
    return final_player
