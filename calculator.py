# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

import json

'''
prints formatted messages 
'''
def prompt(say):
    print(f'==> {say}')

'''
check if input is a proper number 
'''
def invalid_number(num):
    try:
        float(num)
    except(ValueError):
        prompt(get_message('errorvalidnumber'))
        return True
    
    return False

'''
get specified language messages from dictionary
'''
def get_message(message , lang='en'):
    return MESSAGES[lang][message]

MESSAGES = []

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

print(MESSAGES)

prompt(get_message('welcome'))

while True:    
    prompt(get_message('prompt1'))
    num1 = input()
    while invalid_number(num1):
        prompt(get_message('enter'))
        num1 = input()

    prompt(get_message('prompt2'))
    num2 = input()
    while invalid_number(num2):
        prompt(get_message('enter'))
        num2 = input()
        

    prompt(get_message('operationprompt'))

    operation = input()
    while operation not in ['1', '2', '3', '4']:
        prompt(get_message('erroroperation'))
        operation = input()
    '''

    if operation == '1':
        output = int(num1) + int(num2)
    elif operation == '2':
        output = int(num1) - int(num2)
    elif operation == '3':
        output = int(num1) * int(num2)
    elif operation == '4':
        output = int(num1) / int(num2)

    '''
    output = 0
    match operation:
        case '1':
            output = float(num1) + float(num2)
        case '2':
            output = float(num1) - float(num2)
        case '3':
            output = float(num1) * float(num2)
        case '4':
            output = float(num1) / float(num2)

    prompt(get_message('results'))
    prompt(output)
    prompt(get_message('againprompt'))

    
    choice = input()
    while choice.lower() not in ['y', 'n']:
        prompt(get_message('errorvalidchoice'))
        choice = input()
    
    if choice.lower() in 'n':
        break


