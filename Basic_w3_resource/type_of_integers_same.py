#Write a Python program to add two objects if both objects are an integer type.
a = eval(input("Enter the first integer value "))
b = eval(input("Enter the second integer value "))
if type(a)==type(b):
    print("Same objects type")
else:
    print("Different object type, should be int object type only!!")