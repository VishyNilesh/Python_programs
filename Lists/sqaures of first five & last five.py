#Q.16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
l = [x**2 for x in range(1,32)]
t1 = [l[:6]]
t2 = [l[-1:-6:-1]]
print(t1+t2)