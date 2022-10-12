#Q.1. Write a Python script to sort (ascending and descending) a dictionary by value
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
d1={}
l = []
#Ascending order
for x in d:
    l.append(d.get(x))
l.sort()
for y in l:
    for k,v in d.items():
        if y==v:
            d1[k]=y
print('Ascending order',d1)
l.clear()
d1.clear()
#Descending order
for x in d:
    l.append(d.get(x))
l.sort(reverse=True)
for y in l:
    for k,v in d.items():
        if y==v:
            d1[k]=y
print('Descending order',d1)