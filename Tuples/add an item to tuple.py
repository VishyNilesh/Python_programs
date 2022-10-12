#Q.5 Write a Python program to add an item in a tuple.
n = int(input('How many elements you want to add to the tuple : '))
t = tuple([eval(input('Enter the elements in the tuple : '))for x in range(n)])
print(type(t))
print(t)
for x in t:
    print(x,end = ' ')
option = input('Do you want to add more item to tuples : ')
l = []
while option.lower() not in ['NO','N','no','n','No']:
    x = input('Enter the extra item you want to add to tuple : ')
    l.append(x)
    option = input('Do you want to add more item to tuples : ')
final_tuple = t + tuple(l)
print(final_tuple)