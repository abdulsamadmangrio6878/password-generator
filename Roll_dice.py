import random


def roll_dice():
    return random.randint(1, 6)

print("Welcome to the Dice Rolling Simulator!")
while True:
    roll = input("Press Enter to roll the dice or 'q' to quit: ")
    if roll.lower() == 'q':
        break
    else:
        print("You rolled:", roll_dice()) 