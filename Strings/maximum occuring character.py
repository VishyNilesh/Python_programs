#Q.59  Write a Python program to find the maximum occurring character in a given string. Go to the 
s =input('Enter a string : ')
count = 1
alpha = 'No character is repeated more than once'
for x in s:
    if s.count(x)>count:
        count = s.count(x)
        alpha = x
if count>1:
    print(alpha,count)
else:
    print(alpha)