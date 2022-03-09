num = int(input("What is your chosen number?"))
total = 0
for i in range(num + 1):
    total *= i
print("{}! is {}".format(num, total))
