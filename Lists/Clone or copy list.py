#9. Write a Python program to clone or copy a list.
n = int(input('Enter the number of elements you want to add to the lists : '))
l = [eval(input('Enter the item you want to add to the list : ')) for x in range(n)]
l1 = l.copy()
t = l[:]
print(l)
print(type(l))
print(id(l))
print(t)
print(type(t))
print(id(t))