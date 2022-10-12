import csv
with open('emp.csv','r') as f:
    r = csv.reader(f)
    print(r)
    print(type(r))
    data = list(r)
    print(data)
    for x in data:
        for t in x:
            print(t,'\t',end='')
        print()