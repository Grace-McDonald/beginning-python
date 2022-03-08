distance = int(input("How far have you travelled in km? \n"))
hours = int(input("How many hours have you worked? \n"))
parts = int(input("What is the cost of the parts? \n"))
cost_travel = distance * 1.50
cost_lab = hours * 60
total = parts + cost_travel + cost_lab
print("Cost of the travel", cost_travel)
print("Cost of the labor", cost_lab)
print("total cost", total)