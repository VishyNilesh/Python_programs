#Q.49. Write a Python program to count and display the vowels of a given text. 
s = input('Enter the string : ')
l = ['a','e','i','o','u']
count_x = 0
for x in l:
    count_x += s.count(x)
print(count_x)
t = []
for x in s:
    if x in l:
        t.append(x)
print(t)
