#24. Write a Python program to check whether a string starts with specified characters.
s =input('Enter a value')
c = input('Specify the character to check ')
n=len(c)
if s[0:n]==c:
    print("True")
else:
    pass

# we can lso use startswith logic directly
print(s.startswith(c))