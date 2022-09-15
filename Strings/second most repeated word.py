#Q.56 Write a Python program to find the second most repeated word in a given string. ab ca bc ab ca ab bc --> ca
s =input('Enter the string : ')
l = s.split()
t = []
for x in l:
    z = []
    z.append(s.count(x))
    z.append(x)
    if z not in t:
        t.append(z)
t.sort(reverse=True)
random = t[0][0]
print (t)
for y in t:
    if y[0]<random:
        for z in t:
            if z[0]==y[0]:
                print(list(reversed(z)))
        break