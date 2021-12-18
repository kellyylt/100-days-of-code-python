import random
import os
from art import logo, vs
from game_data import data

game_end = False
score = 0


def format_data(choice):
  """Takes randomly generated choice and returns the printable format"""
#Format choice into a printable format
  account_name = choice["name"]
  account_description = choice["description"]
  account_country = choice["country"]
  return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
  """Check if user is correct and return if user got it right"""
#Check if user is correct
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

#Display art
print(logo)
choice_b = random.choice(data)

while game_end != True:
#Generate choice b become choice a
  choice_a = choice_b
  choice_b = random.choice(data)

  while choice_a == choice_b:
    choice_b = random.choice(data)

  print(f"Compare A: {format_data(choice_a)}.")
  print(vs)
  print(f"Against B: {format_data(choice_b)}.")

  #Ask user to guess
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  a_followers = choice_a["follower_count"]
  b_followers = choice_b["follower_count"]

  is_correct = check_answer(guess, a_followers, b_followers)

  #Clear screen
  os.system("clear")
  print(logo)
  
  if is_correct:
    score += 1
    print(f"You're correct. Current score: {score}.")
  else:
    game_end = True
    print(f"Sorry, that's wrong. Final score: {score}.")


