#Q.69 Write a Python program to find the longest common sub-string from two given strings.
''' Original Substrings:   
 abcdefgh
 xswerabcdwd 

 Common longest sub_string:
abcd '''
s1 = input('Enter a string : ')
s2 = input('Enter a string : ')
l = [x for x in s1]
t = [y for y in s2]
print(l)
print(t)
common_l = []
common_t=[]
for element in l:
    if element not in common_l and element in t:
        temp = []
        temp.append(element)
        temp.append(l.index(element))
        common_l.append(temp)
print(common_l)
for element in t:
    if element not in common_t and element in l:
        temp = []
        temp.append(element)
        temp.append(t.index(element))
        common_t.append(temp)
print(common_t)
i = j = 0
str = ''
for ele in l:
    if abs(common_l[i][j]-common_l[i+1][j+1]) == 1:
        str+=common_l[i][j]
        i+=1


