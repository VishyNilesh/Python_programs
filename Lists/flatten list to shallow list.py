#Q.23.Write a Python program to flatten a shallow list. [[2,4,3],[1,5,6], [9], [7,9,0]]-->[2, 4, 3, 1, 5, 6, 9, 7, 9, 0]
n = int(input('How many elements you will add to the list : '))
l = [eval(input()) for x in range(n)]
final = []
i = 0
print(l)
for x in l:
   i = 0
   while i<len(x):
    final.append(x[i])
    i+=1
print(final)