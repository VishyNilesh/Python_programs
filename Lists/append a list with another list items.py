#Q.24.Write a Python program to append a list to the second list.
l1 = [input() for x in range(int(input('How many elements you want to add to the list : ')))]
l2 = [input() for x in range(int(input('How many elements you want to add to the list : ')))]
print(l1)
print(l2)
print(l1.extend(l2))
print(l1)