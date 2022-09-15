''' Q.51 Write a Python program to find the first non-repeating character in given string. wetdo:https://w3resource.com/python-exercises/string/python-data-type-string-exercise-51.php '''
from itertools import count


s = input('Enter the string : ')
for x in s:
    if s.count(x)==1:
       print("The First non repeating charcter is :", x)
       break