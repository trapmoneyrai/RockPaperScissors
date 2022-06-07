import random

while True:
    choices = ["rock", "paper", "scissors"]

    cpu = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Rock, paper or scissors?: ").lower()

    if player == cpu:
        print("cpu: ", cpu)
        print("Player: ", player)
        print("Tie!")
        print("It's either win or lose. Play again.")
    elif player == "rock":
        if cpu == "paper":
            print("cpu: ", cpu)
            print("Player: ", player)
            print("You lost.")
            break
        if cpu == "scissors":
            print("cpu: ", cpu)
            print("Player: ", player)
            print("Winner.")
            break
    elif player == "scissors":
        if cpu == "rock":
            print("cpu: ", cpu)
            print("Player: ", player)
            print("You lost.")
            break
        if cpu == "paper":
            print("cpu: ", cpu)
            print("Player: ", player)
            print("Winner.")
            break
    elif player == "paper":
        if cpu == "scissors":
            print("cpu: ", cpu)
            print("Player: ", player)
            print("You lost.")
            break
        if cpu == "rock":
            print("cpu: ", cpu)
            print("Player: ", player)
            print("Winner.")
            break