#Write a Python program to clone or copy a list
# approach 1
l = []
list_copy=[]
n = int(input("Enter the number of items you want to add to you list "))
for i in range(n):
    x = input('Enter the name of items to be added into your list ')
    l.append(x)
if len(l)!=0:
    print('List is not empty')
    list_copy = l.copy()            #approach2 list_copy = l[:] by using slice operator or # aprroach 3 could be create a new list and copy/append/extend those items to newlist
else:
    print('List is empty ')
print(l)
print(list_copy)
print(id(l))
print(id(list_copy))
