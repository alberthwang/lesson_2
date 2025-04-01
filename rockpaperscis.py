'''
In this assignment, we'll build a Rock Paper Scissors game. Rock Paper Scissors is a simple game played between two opponents. Both opponents choose an item from rock, paper, or scissors. The winner is decided according to the following rules:

    If player a chooses rock and player b chooses scissors, player a wins.
    If player a chooses paper and player b chooses rock, player a wins.
    If player a chooses scissors and player b chooses paper, player a wins.
    If both players choose the same item, neither player wins. It's a tie.

Our version of the game lets the user play against the computer. The game flow should go like this:

    The user makes a choice.
    The computer makes a choice.
    The winner is displayed.

'''
import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
p_wins, c_wins = 0, 0 


def display_winner(choice, computer_choice):
    if ((choice == "rock" and (computer_choice == "scissors" or computer_choice == "lizard")) or
        (choice == "paper" and (computer_choice == "rock" or computer_choice == "spock")) or
        (choice == "scissors" and (computer_choice == "paper" or computer_choice == "lizard")) or
        (choice == "lizard" and (computer_choice == "spock" or computer_choice == "paper")) or
        (choice == "spock" and (computer_choice == "scissor" or computer_choice == "rock"))):
        prompt("You win!")
    elif ((computer_choice == "rock" and (choice == "scissors" or choice == "lizard")) or
        (computer_choice == "paper" and (choice == "rock" or choice == "spock")) or
        (computer_choice == "scissors" and (choice == "paper" or choice == "lizard")) or
        (computer_choice == "lizard" and (choice == "spock" or choice == "paper")) or
        (computer_choice == "spock" and (choice == "scissor" or choice == "rock"))):
        prompt("You lose!")
    else:
        prompt("It's a tie!")

def prompt(message):
  print(f'==> {message}')

def getPlayerChoice():
    def getPlayerInput():
        player_input = input()
        match player_input.lower():
            case 'scissor' | 'sc' | 'sci' | 'scis':
                player_input = 'scissors'
            case 'spock' | 'sp' | 'spco' | 'spoc' | 'spok':
                player_input = 'spock'
            case  'lizard' | 'l' | 'liz' | 'lizd':
                player_input = 'lizard'
            case  'rock' | 'r' | 'ro' | 'rock' | 'roc' | 'rok':
                player_input = 'rock'
            case  'paper' | 'p' | 'pa' | 'pap' | 'pape':
                player_input = 'paper'
            case _:
                prompt("invalid")
                player_input= 'n/a'

        return player_input

    player_choice = getPlayerInput()
    
    while player_choice == 'n/a':
        player_choice = getPlayerInput()

    return player_choice


    # while player_choice not in VALID_CHOICES:
    #   prompt('That is not a valid choice')
    #   player_choice = input()

    # return player_choice
  
while True:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = getPlayerChoice()

    computer_choice = random.choice(VALID_CHOICES)
    prompt(f"You chose {choice}, computer chose {computer_choice}")

    display_winner(choice, computer_choice)
    #if display winner returns a string, i can print that string instead.

    prompt("Do you want to play again (y/n)?")
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break
        
        prompt('Please enter "y" or "n".')
        answer = input().lower()

    if answer[0] == 'n':
        break
