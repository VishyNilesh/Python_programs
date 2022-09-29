# Q2. Write a Python program to multiply all the items in a list.
n = int(input('Enter the number of elements you want to add to the lists : '))
l = [eval(input('Enter the item you want to add to the list : ')) for x in range(n)]
product = 1
for x in l:
    product*=x
print('The product of all elemenmts inside the list is : ', product)