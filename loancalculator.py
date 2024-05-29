'''
You'll need three pieces of information:

    the loan amount
    the Annual Percentage Rate (APR)
    the loan duration

From the above, you'll need to calculate the following two things:

    monthly interest rate
    loan duration in months

    m = p * (j / (1 - (1 + j) ** (-n)))
    
    m = monthly payment
    p = loan amount
    j = monthly interest rate
    n = loan duration in months

'''


monthly_payment = 0



def prompt (prom):
  print(f"==> {prom}")

def invalid_number(num_str):
  try:
    num = float(num_str)
    if num <= 0 :
      raise ValueError(f'value must be > 0')
    
  except ValueError:
    return True

  return False

while True:
  prompt("What is the loan amount?")  
  amount = input()

  while invalid_number(amount):
    amount = input()

  prompt("What is your interest rate?")  
  interest_rate = input()

  while invalid_number(interest_rate):
    interest_rate = input()

  prompt("What is the duration of the loan in years?")  
  loan_duration_years = input()

  while invalid_number(loan_duration_years):
    loan_duration_years = input()


  annual_interest_rate = float(interest_rate) / 100
  monthly_interest_rate = annual_interest_rate / 12
  loan_amount = float(amount)
  months = float(loan_duration_years) * 12

  monthly_payment = loan_amount * ( monthly_interest_rate/(1 - (1 + monthly_interest_rate) ** (-months)))

  prompt(f'Your monthly payment is ${monthly_payment:.2f}')

  prompt('Another calculation?')
  choice = input()

  if choice == 'n':
      break