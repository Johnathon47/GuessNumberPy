import random

name = input("Enter your name: ")


def welcome():
    print("----------------------------------------")
    print(f"       Hello {name} 👋!")
    print("----------------------------------------")
    print("| Welcome in the game 'Guess number' ! |")
    print("----------------------------------------")
    print("I choice number between 1 and 100. try to guess him.")


# Variables
secret_number = random.randint(1, 100)
tries = 0
guess = False


# Guess algorithm
def guessGame(secret_number, tries, guess):
    welcome()
    while not guess:
        proposition = input("Your proposition: ")
        if not proposition.isdigit():
            print("Enter a number valid.")
            continue

        proposition = int(proposition)
        tries += 1

        if proposition < secret_number:
            print(f"Oops! That's number {proposition} is so small 🤏!")
        elif proposition > secret_number:
            print(f"Oops! That's number {proposition} is so big 🥺!")
        else:
            print(f"Great {name} 🥳🪇! You guessed in {tries} tries.")
            guess = True


# Run the Game
guessGame(secret_number, tries, guess)

