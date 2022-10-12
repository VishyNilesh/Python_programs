#Q.4 Write a Python program to unpack a tuple in several variables.
print('Please add 5 elements only to the tuple : ')
t = tuple([eval(input('Enter the elements in the tuple : '))for x in range(5)])
print(type(t))
print(t)
a,b,c,d,e = t
print(a,b,c,d,e)