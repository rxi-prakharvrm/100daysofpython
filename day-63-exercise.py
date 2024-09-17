# Snake Water Gun Game
from random import randint

data_mat = [['d', 'w', 'l'], ['l', 'd', 'w'], ['w', 'l', 'd']]

def num_to_name(choice):
    return "SNAKE" if choice == 0 else "WATER" if choice == 1 else "GUN"

def name_to_num(name):
    return 0 if name.upper() == "SNAKE" else 1 if name.upper() == "WATER" else 2

your_choice = name_to_num(input("Enter your choice('SNAKE', 'WATER', 'GUN'): "))
other_player_choice = randint(0, 2)

if data_mat[your_choice][other_player_choice] == 'w':
    print(f"Congratulations you chose {num_to_name(your_choice)} and other player chose {num_to_name(other_player_choice)}, so you won!")
elif data_mat[your_choice][other_player_choice] == 'l':
    print(f"You chose {num_to_name(your_choice)} and other player chose {num_to_name(other_player_choice)}, so you lost!")
else:
    print(f"You chose {num_to_name(your_choice)} and other player chose {num_to_name(other_player_choice)}, so you math draw!")
