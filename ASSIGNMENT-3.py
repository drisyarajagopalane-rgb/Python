# 1. Set Up the Game:
# Generate a random number between 1 and 10 that the user has to guess. Import random and use randint function.

import random

def play_game():
    secret_number = random.randint(1, 10)
    max_attempts = 5

    for attempt in range(max_attempts):
        guess_text = input("Guess a number from 1 to 10: ")

        if not guess_text.isdigit():
            print("Please enter a whole number.")
            continue

        guess = int(guess_text)

        if guess < 1 or guess > 10:
            print("Your guess must be between 1 and 10.")
            continue

        if guess == secret_number:
            print("Correct!")
            break
        elif guess < secret_number:
            print("Too low.")
        else:
            print("Too high.")
    else:
        print(f"Out of attempts! The number was {secret_number}.")

play_game()

# Ask the user to guess the number.
# Set a variable attempts to 3, which represents the maximum number of guesses allowed
#Use a while loop to allow the user to keep guessing until they get the correct number or run out of attempts.
# Provide feedback to the user for each guess:
# ➢ If the guess is out of the valid range (1 to 10), inform the user.
# ➢ If the guess is greater than the secret number.
# ➢ If the guess is lower than the secret number.
# ➢ If the guess is correct, congratulate the user and end the game.

import random

def play_game():
    secret_number = random.randint(1, 10)
    attempts = 3

    print("I picked a number from 1 to 10.")
    print("You have 3 guesses.")

    while attempts > 0:
        guess_text = input("Guess the number: ")

        if not guess_text.isdigit():
            print("Please enter a whole number.")
            continue

        guess = int(guess_text)

        if guess < 1 or guess > 10:
            print("Please enter a number from 1 to 10.")
            continue

        attempts -= 1

        if guess == secret_number:
            print("Congratulation! You guessed the correct number.")
            break
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")
    else:
        print(f"No guesses left. The number was {secret_number}.")

play_game()

# 4. Control Statements:
# Use continue to skip the rest of the loop after informing the user if the guess is out of range.
# Use break to exit the loop when the guess is correct.
# Use else with the while loop to provide a message like "Better luck next time!" if the user runs out of attempts without guessing the correct number.

import random


def play_game():
    secret_number = random.randint(1, 10)
    attempts = 4

    while attempts > 0:
        guess = int(input("Guess the number (between 1 and 10): "))

        if guess < 1 or guess > 10:
            print("Your guess is out of range. Please guess a number between 1 and 10.")
            continue

        attempts -= 1

        if guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            break
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")
    else:
        print("Better luck next time!")
        print(f"The correct number was {secret_number}.")


play_game()

#For Loop:
# Multiplication Table Generator
# Problem Statement: Create a Python program that generates and prints a
# multiplication table (from 1 to 10) for a given number using a for loop and the range
# function.
# Step wise Instructions:
# 1. Prompt user for Input. Ask the user to enter a number for which they want to generate a multiplication table.
# 2. Generate the Multiplication Table: Use a for loop to iterate through the numbers 1 to 10. In each iteration, calculate the product of the user's number and the
# current number from the loop.
# 3. Display the Multiplication Table: Print each line of the multiplication table in the format: "number x i = result".

def generate_table():
    number = int(input("Enter the number for which you want the multiplication table: "))

    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")


generate_table()


# BMI Calculator
# Problem Statement: Create a Python program that calculates the Body Mass Index (BMI).
# Hint: BMI = weight (kg) / [height (m)]²
# Instructions:
# 1. Define a function calculate_bmi(weight, height) that returns the BMI.
# 2. Prompt the user for their weight (in kg) and height (in meters).
# 3. Use the function to calculate and display the BMI

def calculate_bmi(weight, height):
    return weight / (height ** 2)


weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)

print(f"Your BMI is: {bmi:.2f}")