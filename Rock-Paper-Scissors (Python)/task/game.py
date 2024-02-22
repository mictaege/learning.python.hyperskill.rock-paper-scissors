# Write your code here
import random

cmd_exit = "!exit"
cmd_rating = "!rating"

commands = [cmd_exit, cmd_rating]

default_rules = ["rock", "paper", "scissors"]


def init_usr_rating():
    usr_name = input("Enter your name:")
    print(f"Hello, {usr_name}")
    rating = 0
    with open("rating.txt", "r") as file:
        for line in file:
            data = line.strip().split()
            if data[0] == usr_name:
                rating = int(data[1])
    return rating


def init_rules():
    usr_input = input().strip()
    options = usr_input.split(",") if usr_input != "" else []
    print("Okay, let's start")
    if len(options) == 0:
        return default_rules
    else:
        return options


usr_rating = init_usr_rating()
rules = init_rules()


def play_game(usr_opt):
    global usr_rating
    comp_opt = random.choice(rules)
    if usr_opt == comp_opt:
        print(f"There is a draw ({comp_opt})")
        usr_rating += 50
    else:
        idx = rules.index(usr_opt)
        rotated = rules[idx:] + rules[:idx]
        rotated.pop(0)
        split_idx = len(rotated) // 2
        if rotated.index(comp_opt) < split_idx:
            print(f"Sorry, but the computer chose {comp_opt}")
        else:
            print(f"Well done. The computer chose {comp_opt} and failed")
            usr_rating += 100


def take_input():
    usr_input = input()
    if usr_input not in commands and usr_input not in rules:
        print("Invalid input")
        take_input()
    elif usr_input == cmd_exit:
        print("Bye!")
    elif usr_input == cmd_rating:
        print(f"Your rating: {usr_rating}")
    else:
        play_game(usr_input)
        take_input()


take_input()
