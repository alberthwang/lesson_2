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
player_wins, computer_wins, game_number = 0, 0, 1 


def display_winner(choice, computer_choice):
    if ((choice == "rock" and (computer_choice == "scissors" or computer_choice == "lizard")) or
        (choice == "paper" and (computer_choice == "rock" or computer_choice == "spock")) or
        (choice == "scissors" and (computer_choice == "paper" or computer_choice == "lizard")) or
        (choice == "lizard" and (computer_choice == "spock" or computer_choice == "paper")) or
        (choice == "spock" and (computer_choice == "scissor" or computer_choice == "rock"))):
        return "You win!"
    elif ((computer_choice == "rock" and (choice == "scissors" or choice == "lizard")) or
        (computer_choice == "paper" and (choice == "rock" or choice == "spock")) or
        (computer_choice == "scissors" and (choice == "paper" or choice == "lizard")) or
        (computer_choice == "lizard" and (choice == "spock" or choice == "paper")) or
        (computer_choice == "spock" and (choice == "scissor" or choice == "rock"))):
        return "You lose!"
    else:
        return "It's a tie!"

def prompt(message):
  print(f'==> {message}')

def getPlayerChoice():
    def getPlayerInput():
        player_input = input()
        if player_input in VALID_CHOICES:
            return player_input
        else:
            match player_input.lower():
                case 'scissor' | 'sc' | 'sci' | 'scis':
                    player_input = 'scissors'
                case 'sspock' | 'sp' | 'spco' | 'spoc' | 'spok':
                    player_input = 'spock'
                case  'llizard' | 'l' | 'liz' | 'lizd':
                    player_input = 'lizard'
                case  'rrock' | 'r' | 'ro' | 'rock' | 'roc' | 'rok':
                    player_input = 'rock'
                case  'ppaper' | 'p' | 'pa' | 'pap' | 'pape':
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
  
while (player_wins < 3 and computer_wins < 3):
    winner = ''
    prompt(f'GAME {game_number}')
    prompt(f'Player wins: {player_wins}, Computer wins: {computer_wins}')
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = getPlayerChoice()

    computer_choice = random.choice(VALID_CHOICES)
    prompt(f"You chose {choice}, computer chose {computer_choice}")

    winner = display_winner(choice, computer_choice)
    #if display winner returns a string, i can print that string instead.

    if 'win' in winner:
        prompt(winner)
        player_wins += 1
        game_number += 1
    elif 'lose' in winner:
        prompt(winner)
        computer_wins += 1
        game_number += 1
    else:
        prompt(winner)
        game_number += 1

prompt(f'Final Score: Player wins: {player_wins}, Computer wins: {computer_wins}')

    # prompt("Do you want to play again (y/n)?")
    # answer = input().lower()
    # # while True:
    # #     if answer.startswith('n') or answer.startswith('y'):
    # #         break
        
    # #     prompt('Please enter "y" or "n".')
    # #     answer = input().lower()

    # if answer[0] == 'n':
    #     break
