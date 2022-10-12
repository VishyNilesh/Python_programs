from copy import *
n = int(input('How many elements you want to add to the tuple : '))
t = tuple([input('Enter the elements in the tuple : ')for x in range(n)])
t1 = deepcopy(t)
print(t,id(t))
print(t1,id(t1))
print(t1)