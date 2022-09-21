#Q.58 Write a Python program to move spaces to the front of a given string.
s = input('Enter the string: ')
t=s.count(' ')
print(' '*t + s.replace(' ',''))