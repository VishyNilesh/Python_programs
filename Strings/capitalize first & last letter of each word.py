# 60. Write a Python program to capitalize first and last letters of each word of a given string. 
s = input('Enter the string : ')
l = s.split()
t =[]
for x in l: 
    t.append(x[0].upper() + x[1:len(x)-1] + x[-1].upper())
print(' '.join(t))