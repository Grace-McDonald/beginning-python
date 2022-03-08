rents = int(input("How many videos would you like to rent? "))
if rents >= 10:
    total = 10 + 2 * (rents - 10)
else:
    total = 2 * rents
print("Total cost $", total)
