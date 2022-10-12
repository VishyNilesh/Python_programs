#12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
n = int(input('Enter the number of elements you want to add to the lists : '))
l = [eval(input('Enter the item you want to add to the list : ')) for x in range(n)]
rem = int(input('Enter the number of elements you want to remove from the lists : '))
indices = [eval(input('Enter the index of the item you want to remove from the list : ')) for x in range(rem)]
for x in indices:
    l[x] = ''
c_empty = l.count('')
for i in range(c_empty):
   l.remove('')
print(l)