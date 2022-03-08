side_1 = int(input("What is side one in cm? "))
side_2 = int(input("What is side two in cm? "))
side_3 = int(input("What is side three in cm? "))

if side_1 + side_2 - side_3 > 0 and side_1 + side_3 - side_2 > 0 and side_3 + side_2 - side_1 > 0:
    print(f"You have a triangle with the perimeter of: {side_1 + side_2 + side_3}")
else:
    print("That is not a valid triangle")