#Create Rock Paper Scissors game
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list_of_choice = [rock,paper,scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer_choice = random.randint(0,2)

if player_choice >= 3 or player_choice < 0:
    print("You have entered an invalid number.")
else:
    print(list_of_choice[player_choice])
    print("Computer chose:")
    print(list_of_choice[computer_choice])

    if player_choice == 0 and computer_choice == 2:
        print("You win!")
    elif player_choice == 1 and computer_choice == 0:
        print("You win!")
    elif computer_choice > player_choice:
        print("You lose!")
    elif player_choice > computer_choice:
        print("You win!")
    else:
        print("It's a draw")