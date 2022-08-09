#3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string
x = input("Enter a sample string ")
first_2_char=x[0:2]
last_2_char=x[-2:]
if len(x) < 2:
    print("")
else:
    print(first_2_char + last_2_char)