#Question 1:

top = float(input("Enter the top value"))
bottom = float(input("Enter the bottom value"))
val = float(input("Enter val"))


if val<top and val>bottom:
  print("True")

else:
  print("False")


#Question 2:

a = int(input("Enter the first integer (a)"))
b = int(input("Enter the second integer (b)"))
c = int(input("Enter the third integer (c)"))


print(f"The maximum value is {max(a,b,c)}")
print(f"The minimum value is {min(a,b,c)}")


#question 3:

total_grade = int(input("Enter total grade"))


if total_grade > 89:
    print("A")
elif total_grade > 79:
    print("B")
elif total_grade > 69:
    print("C")
elif total_grade > 59:
    print("D")
else:
    print("F")# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

