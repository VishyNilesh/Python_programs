'''Q.47. Write a Python program to lowercase first n characters in a string.'''
n = int(input('Enter the value of n : '))
s = input('Enter the string : ')
t = ''
i= 0 
while i in range(0,n):
    t+=s[i].lower()
    i+=1
t += s[n:]
print(t)
