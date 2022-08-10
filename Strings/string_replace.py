#7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, 
# if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
s = input('Enter the string ')
print(s.find('not'))
print(s.find('poor'))
i=0
x=0
y=0
new_string=s
while (i!=-1):
    x = s.find('not',y,len(s))
    y = s.find('poor',y,len(s))
    if (x < y) and (x!=-1):
        new_string=new_string.replace(s[x:y+4],'good')
        print(s[x:y+4])
        print(new_string)
        print(x,y)
        y+=4
        i=x
        print(i)
    else:
        break
