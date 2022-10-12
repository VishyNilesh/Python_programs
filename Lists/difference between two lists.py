#Q.19. Write a Python program to get the difference between the two lists
n1 = int(input('Enter the number of elements you want to enter into list 1 : '))
n2 = int(input('Enter the number of elements you want to enter into list 2 : '))
l1 = [input('Enter the number of elements you want to enter into list 1 : ') for x in range(n1)]
l2 = [input('Enter the number of elements you want to enter into list 2 : ') for x in range(n2)]
# for x in l1:
#     if x not in l2:
#         print(x,end =' ')
# for x in l2:
#     if x not in l1:
#         print(x,end =' ')
ans = [x for x in l1 if x not in l2]
ans.extend([x for x in l2 if x not in l1])
print(ans)