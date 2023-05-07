# Number Guessing Game
import random

upper_bound = 100

number = random.randint(1, upper_bound)

print(f'A number between 1 and 100 was just randomly generated.')
print(f'It is your task to find the secret number with as few tries as possible.')

guess = None
count = 1
print(number)
while guess != number:

    guess = int(input(f'Please insert your guess: '))

    if guess == number:
        print(f'Well Done!')

    elif guess < number:
        print(f'The number we´re searching for is greater than your guess.')
        count += 1

    else:
        print(f'The number we´re searching for is smaller than your guess.')
        count += 1
print(f'You needed {count} attempts to find the secret number.')
