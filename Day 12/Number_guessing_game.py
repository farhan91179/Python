import random
from random import randint
from art import logo
print(logo)
print("Welcom to Number Guessing Game!")
print("I'm thinking a number between 1 and 100.")

answer = randint(1, 100)

difficulty  = input("Choose difficulty level, Type 'easy' or 'hard': ")
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 6

chances = False

while not chances:
    print(f"you have {attempts} attempts reamining to guess the number.")
    guess = int(input("Make a guess: "))
    attempts = attempts - 1
    if attempts != 0:
        if guess > 100 or guess < 1:
            print("You chose a number that is out of limit")
            chances = True
        elif guess > answer:
            print("Too high.")
            print("Guess again.")
        elif guess < answer:
            print("Too low.")
            print("Guess again.")
        elif guess == answer:
            print("You guessed it correct.")
            chances = True
    elif attempts == 0:
        print(f"The real value was {answer}. You lose.")
        chances = True





