''' Q.5 Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2 '''
n = int(input('Enter the number of elements you want to add to the lists : '))
l = [(input('Enter the item you want to add to the list : ')) for x in range(n)]
count = 0
for x in l:
    if len(x) > 1 and x[0]==x[-1]:
        count+=1
print('The number of strings whose length is greater than 2 :',count)