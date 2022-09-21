#Q.64 64. Write a Python program to find maximum length of consecutive 0's in a given binary string.
s =input('Enter a binary sting : ')
if '1' in s:
    l=s.split('1')
    count = 0
    string = ''
    print(l)
    for x in l:
        if x.count('0')>count:
            count = x.count('0') 
            string = x
    print(x,count)
else:
    print(s, len(s))