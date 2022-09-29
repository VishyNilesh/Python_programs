#Q.3 Write a Python program to get the largest number from a list.
n = int(input('Enter the number of elements you want to add to the lists : '))
l = [eval(input('Enter the item you want to add to the list : ')) for x in range(n)]
max = l[0]
for x in l:
    if x > max:
        max = x
print('The maximum element inside the list is : ', max)