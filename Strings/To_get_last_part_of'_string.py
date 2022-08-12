''' 19. Write a Python program to get the last part of a string before a specified character. Go to the editor
i/p:https://www.w3resource.com/python-exercises/string
o/p:https://www.w3resource.com/python
Click me to see the sample solution '''
s = input("Enter the string ")
c = input("Enter the Specified character ")
i = s.rfind(c)
print(i)
print(s[i+1:])