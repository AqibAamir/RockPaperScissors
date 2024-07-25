import random

options = ('rock', 'paper', 'scissors')

def get_computer_choice():
    computer_choice = random.choice(options)
    return computer_choice

def get_player_choice():
    while True:
        player_choice = input("What is your choice? (rock, paper, scissors): ").lower()
        if player_choice in options:
            return player_choice
        else:
            print("Invalid choice, please choose rock, paper, or scissors.")

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif player == 'rock':
        if computer == 'scissors':
            return "You win!"
        else:
            return "You lose!"
    elif player == 'paper':
        if computer == 'rock':
            return "You win!"
        else:
