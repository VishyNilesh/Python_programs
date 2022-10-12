#Q.22. Write a Python program to find the index of an item in a specified list list is unique.
n = int(input('How many elements you want to add to the list : '))
l =[input() for x in range(n)]
print(l)
find = input('Enter the element from the list you want to know the index of : ')
print(l.index(find))