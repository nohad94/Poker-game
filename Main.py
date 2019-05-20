import random
from Class import Player
from CARDS import give_card


def player_generator():
    list_name = ["Jim", "Kevin", "Pam", "Michael", "Dwight", "Creed", "Toby", "Oscar", "Meredith", "Stanley", "Angela"]
    player_list = []
    player_list_info = []
    num_user_players = int(input("How many players do you want?: "))
    num_bot_players = int(input("How many bots do you want: "))

    for i in range(num_bot_players):
        player_list.append(Player(random.choice(list_name), 0, True))
    for i in range(num_user_players):
        while num_user_players > 0:
            if num_user_players == 0:
                break
            user_name_choice = input("Choose a name: ")
            player_list.append(Player(user_name_choice, 0, False))
            num_user_players -= 1

    for i in player_list:
        player_info = i.name + " (" + str(i.chip_value) + ") " + str(i.user)
        player_list_info.append(player_info)

    return player_list_info


# print(give_card(player_generator()))


def player_action(lst):
    round_list = lst
    print(round_list)

    for player in round_list:
        player_split = player.split()
        print(player_split)
        if player_split[2] == "False":  # allows players to fold or check
            action = input("What would you like to do?: ")
            if action == "Check":
                pass
            if action == "Fold":
                round_list.remove(player)
                # bots always check
    return round_list


print(player_action(give_card(player_generator())))
# print(player_generator())
