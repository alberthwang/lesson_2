# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

print("Welcome to calculator!")
print("What's the first number?")
num1 = input()
print("what's the second number?")
num2 = input()

print("What is the operation you woulf like to perform? \n 1) Add 2) Subtract 3) Multiply 4) Divide")

operation = input()

if operation == '1':
    output = int(num1) + int(num2)
elif operation == '2':
    output = int(num1) - int(num2)
elif operation == '3':
    output = int(num1) * int(num2)
elif operation == '4':
    output = int(num1) / int(num2)
    
print(f'The result is {output}')