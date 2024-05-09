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

# adding the choices to a list for easier access
choices = [rock, paper, scissors]

# greeting the user
user_choice = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

# generating the computer's choice
computer_choice = random.randint(0, 2)

# printing the choices
print(choices[user_choice] + "\n")

print("Computer chose:\n" + choices[computer_choice])

if user_choice == 0 and computer_choice == 1:
    print("You lose")
elif user_choice == 0 and computer_choice == 2:
    print("You win")
elif user_choice == 1 and computer_choice == 0:
    print("You win")
elif user_choice == 1 and computer_choice == 2:
    print("You lose")
elif user_choice == 2 and computer_choice == 0:
    print("You lose")
elif user_choice == 2 and computer_choice == 1: 
    print("You win")
else: 
    print("Draw") 