"""
CodeOrbit Tech - Python Programming Internship
Task 3: Number Guessing Game

The computer chooses a random number and the player tries
to guess it. The game provides high/low hints, counts attempts,
and supports multiple rounds.
"""

import random


def play_round():
    """Play one round of the number guessing game."""
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\n===== NUMBER GUESSING GAME =====")
    print("I have selected a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Correct! You guessed the number in {attempts} attempts.")
            break


def main():
    """Allow the user to play multiple rounds."""
    while True:
        play_round()

        again = input("\nDo you want to play again? (yes/no): ").strip().lower()

        if again not in ("yes", "y"):
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
