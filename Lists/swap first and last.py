''' Q1 . Given a list, write a Python program to swap first and last element of the list.

Examples: 

Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1] '''
l = []
n =int(input('Enter the number of items you will be adding to the lists : '))
for x in range(n):
    l.append(int(input('Enter the integer items to be added to the list : ')))
print('Before Swapping : ', l)
first_item = l[0]
l[0] = l[-1]
l[-1] = first_item
print('After Swapping : ',l)