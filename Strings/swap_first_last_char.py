#Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
string = input('Enter the string ')
newstring = string[-1] + string[1:len(string)-1]  + string[0]
print(newstring)
