# Q71 .Write a Python program to move all spaces to the front of a given string in single traversal.
s = input ('Enter the string : ')
count = s.count(' ')
print(count * ' ' + s.replace(' ',''))