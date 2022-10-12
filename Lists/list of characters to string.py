#Q.21. Write a Python program to convert a list of characters into a string
n = int(input('Enter how many number of items you want to add to the list : '))
l = [input() for x in range(n)]
print(''.join(l))
for x in l:
    print(x,end='')