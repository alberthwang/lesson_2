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

VALID_CHOICES = ['rock', 'paper', 'scissors']

def display_winner(choice, computer_choice):
    if ((choice == "rock" and computer_choice == "scissors") or
        (choice == "paper" and computer_choice == "rock") or
        (choice == "scissors" and computer_choice == "paper")):
        prompt("You win!")
    elif ((choice == "rock" and computer_choice == "paper") or
          (choice == "paper" and computer_choice == "scissors") or
          (choice == "scissors" and computer_choice == "rock")):
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

def prompt(message):
  print(f'==> {message}')
  
while True:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()

    while choice not in VALID_CHOICES:
      prompt('That is not a valid choice')
      choice = input()

    computer_choice = random.choice(VALID_CHOICES)
    prompt(f"You chose {choice}, computer chose {computer_choice}")

    display_winner(choice, computer_choice)
    #is display winner returns a string, i can print that string instead.

    prompt("Do you want to play again (y/n)?")
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break
        
        prompt('Please enter "y" or "n".')
        answer = input().lower()

    if answer[0] == 'n':
        break
