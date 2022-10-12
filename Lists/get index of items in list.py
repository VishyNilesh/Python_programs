#Q.20 20. Write a Python program access the index of a list.
l = [int(input('Enter the number of elements you want to enter into the list : ')) for x in range(int(input('Enter the number of elements you want to enter into the list : ')))]
i = 0
while i < len(l):
    print(i,'---',l[i])
    i+=1