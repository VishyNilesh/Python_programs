#Q.61 Write a Python program to remove duplicate characters of a given string.
s = input('Enter a string : ')
t = []
for x in s:
    if x not in t:
        t.append(x)
print(''.join(t))
