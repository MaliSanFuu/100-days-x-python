import random
import art

number = random.randint(1,100)

EASY_LEVEL = 10
HARD_LEVEL = 5


def set_difficulty():
    user_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': \t").lower()
    if user_difficulty == "easy":
        return EASY_LEVEL
    elif user_difficulty == "hard":
        return HARD_LEVEL

def game():
    print(art.start)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    lives = set_difficulty()

    guessed = False

    while not guessed and lives > 0:
        user_guess = int(input(f"You've {lives} attempts remaining to guess the number: "))

        if user_guess == number:
            print(f"That is correct! The secret number was {number}")
            guessed = True
        elif user_guess > number:
            print("Too high!")
            lives -= 1
        elif user_guess < number:
            print("Too low!")
            lives -= 1

    if lives == 0:
        print(f"You lost the number was {number}")

game()