''' Q2 Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.
Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]
''' 
n =int(input('Enter the number of items you want to enter into the list : '))
l = [(int(input('Enter the item :'))) for x in range(n)]
pos1  = int(input('Enter the position of element you want to swap :'))
pos2 = int(input('Enter the position of element you want to swap with :'))
l[pos1-1],l[pos2-1] = l[pos2-1],l[pos1-1]
print(l)
