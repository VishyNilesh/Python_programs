#Q.10. Write a Python program to check whether an element exists within a tuple.
n = int(input('How many elements you want to add to the tuple : '))
t = tuple([input('Enter the elements in the tuple : ')for x in range(n)])
print(type(t))
while True:
    x=input('Enter the item you are looking for in the tuple, if not please enter stop : ')
    if x in t:
        print('True')
    elif x.lower()=='stop':
        break
    else:
        print('False')
    

