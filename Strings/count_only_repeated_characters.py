''' 42. Write a Python program to count repeated characters in a string. Go to the editor
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output :
o 4
e 3
u 2
h 2
r 2
t 2 '''

s = input('Enter the string : ')
l=[]
count = 0
for x in s:
   if x not in l:
      l.append(x) 
for item in l:
    count = s.count(item)
    if count>1:
        print(count,item)
    else:
        pass

