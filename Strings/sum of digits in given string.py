#Q.62. Write a Python program to compute sum of digits of a given string. withoutdecimals and in alnum form
s =input ('Enter string : ')
sum = 0
for x in s:
    if x.isnumeric():
        sum+= int(x)
print(sum)