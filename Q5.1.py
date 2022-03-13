total = 0
count = 0
while total < 1000:
    num = int(input("What is the score to be added?"))
    if num == 1000:
        break
    else:
        count += 1
        total += num
average = round(total / count, 2)
print("There were {} scores entered. The total number of runs is {} giving an average {}.".format(count, total, average ))
