# create a simple, rock-paper-scissors game in python
# provide a welcome message and game instruction
# get user input for rock, paper, or scissors
# generate a random choice for the computer
# compare the user's choice with the computer's choice and determine the winner 
# display the result of the game
# ask the user if they want to play again
# if yes, repeat the game, if no, exit the game

import random

def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:        return "Computer wins!"

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    print("Instructions: Enter 'rock', 'paper', or 'scissors' to play.")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break
        
if __name__ == "__main__":    
    play_game()   
