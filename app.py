from lobby import *

APP_NAME = "Poker Game"

if __name__ == "__main__":
    print(f"Starting {APP_NAME}")
    # do stuff here
    num_user_players = input("How many players do you want?: ")
    num_bot_players = input("How many bots do you want: ")
    lobby = Lobby(num_user_players, num_bot_players)
    lobby.init_lobby(5000)
    lobby.start_round()
    print(f"Lobby: {lobby}")
