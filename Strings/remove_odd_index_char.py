#11. Write a Python program to remove the characters which have odd index values of a given string.
string = input('Enter the string ')
newstring = ''
i=0
while i<len(string):
    if i%2==0:
        newstring+=string[i]
    i+=1
print(newstring)
