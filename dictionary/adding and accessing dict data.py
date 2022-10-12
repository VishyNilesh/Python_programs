rec = {}
n = int(input('Enter number of students : '))
i=1
while i<=n:
    name = input('Enter the name of student : ')
    marks = input('Enter the marks for students :')
    rec[name] = marks
    i+=1
print('Name','|','Marks')
print('-'*30)
for x in rec:
    print(x,'|',rec[x])
