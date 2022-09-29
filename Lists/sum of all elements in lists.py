# Q1.Write a Python program to sum all the items in a list
n =int(input('Enter the number of elements you add to the lists: '))
l = [eval(input('Enter the items you want to add to the list : ')) for x in range(n)]
sum = 0
for x in l:
    sum+=x
print('The sum of list is : ', sum)