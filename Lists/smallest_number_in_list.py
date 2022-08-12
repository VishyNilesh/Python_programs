#4. Write a Python program to get the smallest number from a list.
count = int(input("How many list of number you want to add to the list "))
l=[]
for i in range(count):
    x = int(input('Enter the number'))
    l.append(x)
smallest=l[0]
for i in l:
    if i<smallest:
        smallest=i
print('the smallest of numbers provided is {}'.format(smallest))