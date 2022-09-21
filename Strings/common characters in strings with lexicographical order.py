#Q.65 Write a Python program to find all the common characters in lexicographical order from two given lower case strings. If there are no common letters print “No common characters”.

s1 = input('Enter The string1 : ')
s2 = input('Enter the string2 : ')
l = []
t = []
for x in s1:
    if x in s2 and x not in l:
        l.append(x)
t = sorted(l)
print(t)


