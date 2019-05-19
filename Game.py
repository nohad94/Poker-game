import random
from Class import Player
from CARDS import give_card


def player_generator():
    list_name = ["Jim", "Kevin", "Pam", "Michael", "Dwight", "Creed", "Toby", "Oscar", "Meredith", "Stanley", "Angela"]
    player_list = []
    player_list_info = []
    num_user_players = int(input("How many players do you want?: "))
    num_bot_players = int(input("How many bots do you want: "))
    user_name_choice = input("Choose a name: ")

    for i in range(num_bot_players):
        player_list.append(Player(random.choice(list_name), 0, True))
    for i in range(num_user_players):
        player_list.append(Player(user_name_choice, 0, False))

    for i in player_list:
        player_info = "Player name: " + i.name + "(" + str(i.chip_value) + ")"
        player_list_info.append(player_info)

    return player_list_info


print(give_card(player_generator()))
