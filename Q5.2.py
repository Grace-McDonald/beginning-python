total = 0
while total < 200:
    num = int(input("please enter a number between 50 and 100: "))
    if num >= 50 and num <= 100:
        total += num
    else:
        print("That's not a valid number")
print("The grand total is {}".format(total))