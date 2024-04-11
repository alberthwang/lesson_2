# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

def prompt(say):
    print(f'==> {say}')

def invalid_number(num):
    try:
        int(num)
    except(ValueError):
        prompt('invalid input')
        return True
    
    return False
    
prompt("Welcome to calculator!")
prompt("What's the first number?")
num1 = input()
while invalid_number(num1):
    prompt('Enter a number')
    num1 = input()

prompt("what's the second number?")
num2 = input()
while invalid_number(num2):
    prompt('Enter a number')
    num2 = input()
    

#prompt("What is the operation you woulf like to perform? \n 1) Add 2) Subtract 3) Multiply 4) Divide")

operation = input()
while operation not in ['1', '2', '3', '4']:
    prompt('You must choose 1, 2, 3, or 4. \n1) Add 2) Subtract 3) Multiply 4) Divide')
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
        output = int(num1) + int(num2)
    case '2':
        output = int(num1) - int(num2)
    case '3':
        output = int(num1) * int(num2)
    case '4':
        output = int(num1) / int(num2)

    



prompt(f'The result is {output}')