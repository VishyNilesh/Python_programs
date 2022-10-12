#Q.6. Write a Python program to convert a tuple to a string.
n = int(input('How many elements you want to add to the tuple : '))
t = tuple([eval(input('Enter the elements in the tuple : '))for x in range(n)])
print(type(t))
s=''.join(t)
print(s)
print(type(s))
