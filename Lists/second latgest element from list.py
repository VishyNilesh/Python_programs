#Q. 27. Write a Python program to find the second smallest number in a list
l = [eval(input('Enter the item into the list ')) for x in range(int(input('How many elements you want to add to the list : ')))]
print(l.sort())
min = min(l)
for x in l:
    if x!=min:
        break
print('The second smallest number inside the list is : ',x)
