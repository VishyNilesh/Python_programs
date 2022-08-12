#7. Write a Python program to remove duplicates from a list. 
# At the time of making list iteslf
l = []
n = int(input("Enter the number of items you want to add to you list "))
for i in range(n):
    x = input('Enter the items to be added into your list ')
    if x not in l:
        l.append(x)
print(l)
# After fomrmation of list
l = []
u= []
n = int(input("Enter the number of items you want to add to you list "))
for i in range(n):
    x = input('Enter the items to be added into your list ')
    l.append(x)
for x in l:
    if x not in u:
        u.append(x)
print(l)
print(u)
