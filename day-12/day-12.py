from random import randint
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(guess, number, turns):
    """Checks answer against guess. Returns number of turns remaining"""
    if guess > number:
        print("Too high.\nGuess again.")
        return turns - 1
    elif guess < number:
        print("Too low.\nGuess again.")
        return turns - 1
    else:
        print(f"You got it! The answer was {number}. You win!")

def set_difficulty():
    """Return difficulty based on global variable set"""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_LEVEL
    elif difficulty == "hard":
        return HARD_LEVEL

def game():
    print(logo)
    number = randint(1,100)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")
    turns = set_difficulty()

    guess = 0
    while guess != number:
        print(f"You'll have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, number, turns)
        
    if turns == 0:
        print("You've run out of guesses, you lose.")
    if guess != number:
        print("Guess again.")

game()