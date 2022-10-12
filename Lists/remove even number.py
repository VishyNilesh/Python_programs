#Q.14. Write a Python program to print the numbers of a specified list after removing even numbers from it
n = int(input('Enter number of elements you want to add to the list : '))
l = [eval(input('Enter the items : '))for i in range(n)]
ans = []
for x in l:
    if x%2!=0:
        ans.append(x)
print(ans)