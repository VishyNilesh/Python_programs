#1. Write a Python program to sum all the items in a list.
count = int(input("How many list of number you want to add "))
l=[]
sum = 0
for i in range(count):
    x = int(input('Enter the number'))
    l.append(x)
    sum += l[i]
print('the sum of numbers provide is {}'.format(sum))