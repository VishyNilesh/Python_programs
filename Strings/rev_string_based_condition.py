#20. Write a Python function to reverses a string if it's length is a multiple of 4. 
s = input('Enter the string ')
if len(s)%4==0:
    print(s[::-1])
else:
    pass