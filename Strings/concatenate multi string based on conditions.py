#Q.68 Write a Python program to create two strings from a given string. Create the first string using those character which occurs only once and create the second string which consists of multi-time occurring characters in the said string
s  = input ('Enter the string : ')
non_repeat = ''
repeat = []
for x in s:
    if s.count(x)==1:
        non_repeat+=x
    elif x not in repeat:
        repeat.append(x)
print(non_repeat)
print(''.join(sorted(repeat)))