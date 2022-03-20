from importlib.util import find_spec


first_name = input("What is your fist name? ")
last_name = input("What is your last name? ")
first_name1 = first_name[1:].upper() + first_name[2:].lower()
last_name2 = last_name[1:].upper() + last_name[2:].lower()
print(f"hello, {first_name}, {first_name1}, {last_name}, {last_name2}")
# I have come to the conclusion that I am to tired for this...