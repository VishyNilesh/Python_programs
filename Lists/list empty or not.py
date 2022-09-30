#Q.8 Write a Python program to check a list is empty or not
n = int(input('Enter the number of elements you want to add to the lists : '))
l = [eval(input('Enter the item you want to add to the list : ')) for x in range(n)]
if len(l)!=0:
    print('List is not empty !',l)
else:
    print('List is empty',l)