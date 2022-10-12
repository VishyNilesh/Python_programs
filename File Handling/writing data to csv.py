import csv
with open('emp.csv','w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['E-no','E-Name','E-Sal','E-Address'])
    n=int(input('Enter the count for employees data you want to fill : '))
    for i in range(n):
        eno = input('Enter employee number : ')
        ename = input('Enter employee name : ')
        esal = input('Enter employee salary : ')
        eadd = input('Enter employee location : ')
        w.writerow([eno,ename,esal,eadd])
print('Total data inserted into csv file successfully!')