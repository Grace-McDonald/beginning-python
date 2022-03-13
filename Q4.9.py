import math
pi = math.pi
print("radius:  circumference:  area:")
for r in range(10, 101, 10):
    circumference = round(2 * pi * r, 2)
    area = round(pi * r ** 2, 2)
print("{}           {}          {}".format(r, circumference, area))