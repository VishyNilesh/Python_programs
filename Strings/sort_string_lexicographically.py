#22.Write a Python program to sort a string lexicographically.
s =input('Enter a value')
print(sorted(sorted(s),key=str.upper))