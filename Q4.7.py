num = int(input("What is your chosen number?"))
total = 1
for i in range(1,num + 1):
    total *= i
print("{}! is {}".format(num, total))