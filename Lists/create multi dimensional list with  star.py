#Q.13. Write a Python program to generate a 3*4*6 3D array whose each element is *.
row = int(input('Enter the number of rows'))
column = int(input('Enter the number of rows'))
items = int(input('Enter the number of rows'))
outerouterlist =[]
outerlist = []
inner1 = []
for i in range(row):
    inner1 = []
    for j in range(column):
            inner =[]
            for k in range(items):
                inner.append('*')
            inner1.append(inner)
    outerlist.append(inner1)
print(outerlist)