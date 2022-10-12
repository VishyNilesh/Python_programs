#Q9. Write a Python program to find the repeated items of a tuple.
n = int(input('How many elements you want to add to the tuple : '))
t = tuple([(input('Enter the elements in the tuple : '))for x in range(n)])
count = 0
l=[]
for x in t:
    if t.count(x) > 1 and x not in l:
        l.append(x)
        count+=1
print('Total number of repeated items in tuple are : ',count)
print('Repeated items of the tuple are : ', l)
for x in l:
    print(f'{x} is repeated {t.count(x)} times')