#Q.7. Write a Python program to get the 4th element and 4th element from last of a tuple.
n = int(input('How many elements you want to add to the tuple : '))
t = tuple([input('Enter the elements in the tuple : ')for x in range(n)])
first_element,last_element = t[3],t[-4]
print(first_element,'---',last_element)