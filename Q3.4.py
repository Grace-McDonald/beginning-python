gas = float(input("How many liters of gas do you use per month? (in liters) "))
if gas < 55:
    print("you use:", (gas * 7.45) ,"$ dollars")
else:
    if gas >= 55:
        print("You use", (gas * 6.85),"$ dollars")
    