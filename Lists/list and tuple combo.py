''' Q. 6 Write a Python program to get a list, sorted in increasing order by the last element in each tuple 
from a given list of non-empty tuples. Go to the editor
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''
n = int(input('Enter the number of elements you want to add to the lists : '))
l = [eval(input('Enter the item you want to add to the list : ')) for x in range(n)]
t=[]
for x in l:
    if x[1] not in t:
        t.append(x[1])
t.sort()
final =[]
for x in t:
    for i in range(0,5):
        if x == l[i][1]:
            print(l[i][1])
            final.append(l[i])
print(final)