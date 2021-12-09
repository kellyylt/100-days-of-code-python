#Create a calculator
from art import logo
import os

#Addition
def add(n1, n2):
  return n1 + n2

#Subtraction
def subtract(n1,n2):
  return n1 - n2

#Division
def divide(n1, n2):
  return n1 / n2

#Multiplication
def multiply(n1,n2):
  return n1 * n2

#Create dictionary
operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

#Create function for main logic
def calculator():

  print(logo)

  num1 = float(input("What's the first number? : "))
  for operation in operations:
    print(operation)
  to_continue = True

  while to_continue:
    operation_symbol = input("Pick an operation:")
    num2 = float(input("What's the next number? : "))
    answer = operations[operation_symbol](num1,num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ") == 'y':
      num1 = answer
    else:
      to_continue = False
      os.system("clear")
      calculator()

calculator()