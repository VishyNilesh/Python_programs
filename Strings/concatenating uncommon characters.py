#Q.70. Write a Python program to create a string from two given strings concatenating uncommon characters of the said strings.
s1 = input('Enter the string : ')
s2 = input('Enter the string : ')
l = [x for x in s1 if x in s1 and x not in s2]
t = [y for y in s2 if y in s2 and y not in s1]
print(''.join(l) + ''.join(t))


