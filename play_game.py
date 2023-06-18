import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Enter your guess (1-100): "))
        attempts += 1

        if guess == secret_number:
            print("Congratulations! You guessed the number in", attempts, "attempts.")
            break
        elif guess < secret_number:
            print("Too low. Try again!")
        else:
            print("Too high. Try again!")

print("Welcome to the Number Guessing Game!")
play_game()