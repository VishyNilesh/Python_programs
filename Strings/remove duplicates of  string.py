#Q.67. Write a Python program to remove all consecutive duplicates of a given string. xxxxxyyyyy-->xy
s = input('Enter the string : ')
t = s[0]
i = 0
while i < (len(s)-1):
    if s[i]!=s[i+1]:
        t+=s[i+1]
    i+=1
print(t)

