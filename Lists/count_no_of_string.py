''' 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are 
same from a given list of strings. Go to the editor
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2 '''
l = []
n = int(input("Enter the number of items you want to add to you list "))
count = 0
for i in range(n):
    x = input('Enter the name of items to be added into your list ')
    l.append(x)
print()
for x in l:
    if len(x)>=2 and x[0]==x[-1]:
        count+=1
print(count)
