#Q.72 Write a Python code to remove all characters except a specified character in a given string.
''' Original string
google
Remove all characters except g in the said string:
gg '''
s = input('Enter the string : ')
not_remove = input ('Enter the character you want to keep : ')
t = ''
for x in s:
    if x == not_remove:
        t+=x
    else:
        pass
print(t)
