num1 = int(input("What is number 1? "))
num2 = int(input("What is number 2? "))
total = num1 + num2 
if num1 > num2:
    print(f"These are your numbers: {num1} and {num2} your first number is bigger")
if num1 < num2:
    print(f"These are your numbers: {num1} and {num2} your second number is bigger")
else:
    print(f"These are your numbers: {num1} and {num2} your numbers are equal")

print(f"This is your total for your two numbers: {total}")