from distutils.command.build_scripts import first_line_re
from re import U


first_name, second_name = input("What is your first and last name ").split(" ")
print(first_name)
print(second_name)
username = second_name[0:5] + first_name[0]
print(username.lower())