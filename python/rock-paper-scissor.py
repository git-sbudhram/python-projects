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

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Sciccors\n"))
if user_input >= 3 or user_input < 0:
  print("Invalid number, you lose")
else:  
  player1 = user_input
  choices = [rock, paper, scissors]
  computer = random.randint(0, 2)

  player_choice = choices[user_input]
  computer_choice = choices[computer]

  print(player_choice)

  print("Computer chose: \n")

  print(computer_choice)

  if player1 == 0 and computer == 2:
    print("You win!")
  elif computer == 0 and player1 == 2:
    print("You lose!")
  elif computer > player1:
    print("You lose!")
  elif player1 > computer:
    print("You win!")
  elif player1 == computer:
    print("It's a draw!")
