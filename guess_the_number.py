import random

secret_number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10:"))

if guess == secret_number:
    print("You guessed right!")
elif guess > secret_number:
    print("Too high! The number was", secret_number)
else:
    print("Too low! The number was", secret_number)


