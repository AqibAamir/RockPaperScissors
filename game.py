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
            return "You lose!"
    elif player == 'scissors':
        if computer == 'paper':
            return "You win!"
        else:
            return "You lose!"

def play_again():
    while True:
        play_again_choice = input("Do you want to play again? (yes/no): ").lower()
        if play_again_choice in ('yes', 'no'):
            return play_again_choice == 'yes'
        else:
            print("Invalid choice, please enter 'yes' or 'no'.")

def play_game():
    while True:
        computer_choice = get_computer_choice()
        player_choice = get_player_choice()
        
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        print(result)
        
        if not play_again():
            break

play_game()


