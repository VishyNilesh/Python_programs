''' 18. Write a Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string. Go to the editor
Sample function and result :
first_three('ipy') -> ipy
first_three('python') -> pyt
Click me to see the sample solution '''
s = input("Enter the string ")
if (len(s)>=3):
    print(s[:3])
else:
    pass