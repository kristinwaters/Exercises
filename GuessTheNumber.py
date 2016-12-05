# @author: Kristin Dahl
# December 4, 2016
import random

while True:
    # Select random number
    random.seed(None)

    random_number = random.randint(1, 100)
    print("Psst...answer is: " + str(random_number))
    user_input = int(input("Guess a number between 1 and 100: "))

    while True:
        if user_input > random_number:
            user_input = int(input("Too high. Guess again: "))
        elif user_input < random_number:
            user_input = int(input("Too low. Guess again: "))
        else:
            break

    if input("Yay you win. Play again? (y/n) ") == "n":
        break
