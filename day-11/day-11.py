############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import random
import os
from art import logo

def deal_card():
  """Returns random card from deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  chosen_card = random.choice(cards)
  return chosen_card

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []
def calculate_score(list_of_cards):
  """Take list of cards and sum up the score"""
  if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
    return 0
  elif sum(list_of_cards) > 21 and 11 in list_of_cards:
    list_of_cards.remove(11)
    list_of_cards.append(1)
    return sum(list_of_cards)
  else:
    return sum(list_of_cards)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over 21. You lose!"
  if user_score == computer_score:
    return "It's a draw."
  elif computer_score == 0:
    return "You lose! The computer has a Blackjack."
  elif user_score == 0:
    return "You win with a Blackjack!"
  elif user_score > 21:
    return "You went over 21. You lose!"
  elif computer_score > 21:
    return "The computer went over 21. You win!"
  elif user_score > computer_score:
    return "You win!"
  else:
    return "You lose!"

def play_game():
  print(logo)

  user_cards = [deal_card(), deal_card()]
  computer_cards = [deal_card(), deal_card()]
  game_ends = False

  while not game_ends:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards : {user_cards}, current score: {user_score}")
    print(f"Computer's first hand : {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_ends = True
    else:
      if input("Do you want to draw another cards? Type 'y' for yes and 'n' for no.") == "y":
        user_cards.append(deal_card())
      else:
        game_ends = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' for yes and 'n' for no.") == "y":
  os.system("clear")
  play_game()