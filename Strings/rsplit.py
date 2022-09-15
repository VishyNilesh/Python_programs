#Q.50 Write a Python program to split a string on the last occurrence of the delimiter. "w,3,r,e,s,o,u,r,c,e"-->['w,3,r,e,s,o,u,r,c', 'e'] 
s =input('enter the string : ')
n = int(input('Enter the delimiter value ffrom back/lst occureneces to split'))
print(s.rsplit(',',n))
