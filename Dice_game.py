"""Write a program to simulate a roll of a die/dice A die has 6 faces with numbers 1 to 6 written on them,The program should
randomly print's a number between 1 and 6."""

import random
print("Welcome to the game of rolling a dice")

while True:
    choice = input("Press 'Enter' to roll the dice or 'q' to quit.")
    choice = choice.strip()   #OPTIONAL TO AVOID THE SPACE-BAR ERROR.
    if choice == "q":
        print("Thanks for playing the game, bye!")
        break
    elif choice == '':
        number = random.randint(1, 6)
        print(f"Your number is {number}")
    else:
        print("Invalid input!!")
print("GAME OVER!!")