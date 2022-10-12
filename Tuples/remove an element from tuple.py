#Q.12. Write a Python program to remove an item from a tuple.
n = int(input('How many elements you want to add to the tuple : '))
t = [input('Enter the elements in the tuple : ') for x in range(n)]
print(tuple(t))
item = input('Specify the item you want to remove from tuple : ')
#print(type(t))
t.remove(item)
print('After removing the specified element from tuple the tuple looks like this : ')
t = tuple(t)
print(t)
print(type(t))