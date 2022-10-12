#Q.17 Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).
l = [x**2 for x in range(1,32)]
t1 = l[5:]
print(t1)