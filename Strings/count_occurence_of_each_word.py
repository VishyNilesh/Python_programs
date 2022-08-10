#12. Write a Python program to count the occurrences of each word in a given sentence
string = input('Enter the string separated by space ')
l = string.split()
d={}
for x in l:
    if x not in d:
        d[x]=1
    else:
        d[x]+=1
print(d)
