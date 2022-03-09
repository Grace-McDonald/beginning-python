num = int(input("What is your chosen number?"))
total = 0
for i in range(num + 1):
    total += i
print("adding the numbers from 1 to {} gives {} ".format(num, total))
