#2. Write a Python program to count the number of characters (character frequency) in a string. 
s = input("Enter the string ")
d= {}
for x in s:
    if x in d:
        d[x]+=1
    else:
        d[x]=1
print(d)