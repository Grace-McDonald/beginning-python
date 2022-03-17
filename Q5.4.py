fruit = "Apple"
guess = input("guess the fruit! \n")
guesses = 1
while guess != fruit:
    print("no that wasn't it")
    guess = input("guess the fruit! \n")
    guesses += 1
print("Well done you got it!")
print("it took {} guess".format(guesses))