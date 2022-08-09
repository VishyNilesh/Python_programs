#40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
import math
x1=eval(input("Enter x1 distance "))
y1=eval(input("Enter y1 distance "))
x2=eval(input("Enter x2 distance "))
y2=eval(input("Enter y2 distance "))
distance = math.sqrt((x1-x2)**2+(y1-y2)**2)
print(round(distance,2))