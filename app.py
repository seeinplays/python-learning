import math
from tkinter.tix import INTEGER

## INPUT
# name = input("What is your name? ")
# print("Hello " + name)

## INTEGER
# birth_year = input("Type your year of birth? ")
# age = 2022 - int(birth_year)

# print("Your age is " + age)

# # FLOAT
# first = input("first ")
# second = input("second ")

# sum = float(first) + float(second)

# print("Sum is " + str(sum))

# # STRINGS
# course = "Python Tutorial for you"
# print(course.upper())
# print(course.find("t"))
# print(course.replace("for", "x"))
# print("Python" in course)


# # LOGICAL OPERATORS
# price = 25
# print(price > 10 and price < 30)
# print(price > 10 or price < 30)
# print(not price > 10)


# IFs
weight = input("Weight: ")
unit = input("(K)g or (L)bs: ")

if unit.upper() == "K":
    converted = float(weight) / 0.45
    print("Weight in Lbs : " + str(converted))
elif unit.upper() == "L":
    converted = float(weight) * 0.45
    print("Weight in Kgs : " + str(converted))
else: 
    print("Not a valid weight type.")

    

