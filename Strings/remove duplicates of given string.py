#Q.66 . Write a Python program to make two given strings (lower case, may or may not be of the same length) anagrams removing any characters from any of the strings
s1 = input('Enter a string : ')
s2 = input('Enter a string : ')
t1=[]
for x in s1:
    if x in s2:
     t1.append(x) 
print(t1)
print((len(s1)-len(t1)) + (len(s2)-len(t1)))