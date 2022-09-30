#11. Write a Python function that takes two lists and returns True if they have at least one common member.

n1 = int(input('Enter the number of elements you want to add to the lists : '))
l1 = [eval(input('Enter the item you want to add to the list : ')) for x in range(n1)]
n2 = int(input('Enter the number of elements you want to add to the lists : '))
l2 = [eval(input('Enter the item you want to add to the list : ')) for x in range(n2)]

if len(l1) !=0 and len(l2)!=0:
    for x in l1:
        if x in l2:
            print('True')
            break
        elif x not in l2 and x == l1[-1]:
            print('False')
else:
    print('one or both of the list are empty!')