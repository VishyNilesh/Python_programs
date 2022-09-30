#Q.7. Write a Python program to remove duplicates from a list.
n = int(input('Enter the number of elements you want to add to the lists : '))
l = [eval(input('Enter the item you want to add to the list : ')) for x in range(n)]
print(list(set(l))) # using set its very easy

#other approach is

t = []
for x in l:
    if x not in t:
        t.append(x)
print(t)