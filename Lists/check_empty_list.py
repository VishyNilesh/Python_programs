#8. Write a Python program to check a list is empty or not. 
l = []
n = int(input("Enter the number of items you want to add to you list "))
for i in range(n):
    x = input('Enter the name of items to be added into your list ')
    l.append(x)
if len(l)!=0:
    print('List is not empty')
else:
    print('List is empty ')