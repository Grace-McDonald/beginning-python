length = int(input("How many numbers do you wish to see? ")) 

num1 = 1
num2 = 1
if length >= 1:
    print(num1)
if length >= 2:
    print(num2)
for i in range(length - 2):
    total = num1 + num2
    print(total)
    num1 = num2
    num2 = total