#9. Write a Python program to remove the nth index character from a nonempty string. Go to the 
string = input('Enter the string ')
pos = int(input('Specify the position of element you want to remove from the given string whose length is {}'.format(len(string))))
s=string.replace(string[pos],'')
print(s)
