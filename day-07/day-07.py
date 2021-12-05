#Create hangman game

import random
from hangman_words import word_list
from hangman_art import stages, logo

#Import word list
word_list = word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Initiate lives
end_of_game = False
lives = 6

#Print hangman logo
print(logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Remind user if a letter has been guessed
    if guess in display:
      print(f"You've chosen letter {guess}. This has already been guessed.")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #Tell user the wrong letter chosen
        print(f"You've chosen letter {guess}. This is not in the word, you will lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a string
    print(f"{' '.join(display)}")

    #Check if user has got all letters
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #Pring hangman picture
    print(stages[lives])