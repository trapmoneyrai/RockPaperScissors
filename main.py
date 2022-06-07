import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Rock, paper or scissors?: ").lower()

    if player == computer:
        print("Computer: ", computer)
        print("Player: ", player)
        print("Tie!")
        print("It's either win or lose. Play again.")
    elif player == "rock":
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lost.")
            break
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Winner.")
            break
    elif player == "scissors":
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lost.")
            break
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Winner.")
            break
    elif player == "paper":
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lost.")
            break
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Winner.")
            break