#Q.55 Write a Python program to find the first repeated word in a given string. ab ca bc ab ca ab bc --> ab
s =input('Enter the string : ')
l = s.split()
for x in l:
    if l.count(x)>1:
        print(x)
        break
    else:
        if x == l[-1]:
            print('None')