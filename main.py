from Data import data
import random
import os
from Art import logo, vs


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_account():
    return random.choice(data)


def show_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    score = 0
    continue_game = True

    account_a = get_account()
    account_b = get_account()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    while continue_game:
        if a_follower_count > b_follower_count:
            account_b = get_account()
        else:
            account_a = account_b
            account_b = get_account()

        while account_a == account_b:
            account_b = get_account()

        print(f"compare A : {show_data(account_a)} , ")
        print(vs)
        print(f"Against B : {show_data(account_b)} , ")

        guess = input("who has more followers ? Type 'A' or 'B'").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        correct = check_answer(guess, a_follower_count, b_follower_count)

        clear()

        if correct:
            score += 1
            print(f"You're right ! current score : {score}.")
        else:
            continue_game = False
            print(f"Sorry , You're wrong . Your final score is {score}")


game()
