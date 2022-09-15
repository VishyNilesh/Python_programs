#Q.54 Write a Python program to find the first repeated character of a given string where the index of first occurrence is smallest.
''' ('a', 0)
('b', 1)
('c', 2)
('x', 3) '''
s = input("Enter a string : ")
t = ''
for z in s:
    if z not in t:
        t+=z

for x in t:
    if s.count(x)>1:
        print(x ,end =',')
        print(s.find(x))
    else:
        if x == t[-1]:
            print('None')
