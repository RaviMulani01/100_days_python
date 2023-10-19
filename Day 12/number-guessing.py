import random

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "hard":
    attempts = 5
else:
    attempts = 10

def number_guess(attempts):
    number = random.randint(1,101)

    while True:

        if attempts == 0:
            print(f"Game Over, You have {attempts} attempts remaining to guess the number.")
            return

        else:
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess = int(input("Make a Guess: "))

            if guess == number:
                print(f"You got it! The answer was {guess}.")
                return

            elif guess > number:
                print("Too high.")

            elif guess < number:
                print("Too low.")
            
            attempts -= 1

            if attempts != 0:
                print("Guess Again!")

number_guess(attempts)