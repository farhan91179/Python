# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random
you = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
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

xyz = [rock, paper, scissors]
computer_guess = random.randint(0, 2)

if you > 2 or you < 0:
    print("You typed an invalid number, you lose!")
else:
    print(xyz[you])
    print("Computer chose")
    print(xyz[computer_guess])

    if computer_guess == you:
        print("It's a draw")
    elif computer_guess == 0 and you == 1:
        print("You Win!")
    elif computer_guess == 0 and you == 2:
        print("You lose")
    elif computer_guess == 1 and you == 0:
        print("You lose")
    elif computer_guess == 1 and you == 2:
        print("You win!")
    elif computer_guess == 2 and you == 0:
        print("You win!")
    elif computer_guess == 2 and you == 2:
        print("You lose")