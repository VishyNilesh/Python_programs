#2. Write a Python program to multiply all the items in a list. 
count = int(input("How many list of number you want to multiply "))
l=[]
prod = 1
for i in range(count):
    x = int(input('Enter the number'))
    l.append(x)
    prod *= l[i]
print('the product of numbers provide is {}'.format(prod))