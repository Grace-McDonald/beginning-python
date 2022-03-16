import random

num = random.randrange(1, 10)
guess = int(input("Guess the number"))
while guess != num:
    if guess > num:
        print("Your guess was to high")
    if guess < num:
        print("Your guess was to low")
    guess = int(input("Guess the number"))

