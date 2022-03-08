curtain_m = 6.50
cpm = int(input("How much is your cloth per m? \n"))
meters = int(input("How many meters? \n"))
cost_cloth = meters * cpm
cost_labor = meters * 6.50
total_cost = cost_labor + cost_cloth + 45
print("Cost of cloth", cost_cloth)
print("Cost of labor", cost_labor)
print("Total cost", total_cost)