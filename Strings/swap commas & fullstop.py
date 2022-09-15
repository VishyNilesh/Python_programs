''' Q.48  Write a Python program to swap comma and dot in a string. Go to the editor
Sample string: "32.054,23"
Expected Output: "32,054.23" '''
s = input("Enter the string : ")
t = ''
for x in s:
    if x == ',':
        t += '.'
    elif x== '.':
        t+= ','
    else:
        t+=x
print(t)
