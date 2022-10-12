#Q.3 Write a Python program to create a tuple with numbers and print one item.
n = int(input('How many elements you want to add to the tuple : '))
t = tuple([eval(input('Enter the elements in the tuple : '))for x in range(n)])
print(type(t))
print(t)
for x in t:
    print(x,end = ' ')