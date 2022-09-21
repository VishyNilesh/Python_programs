#Q.45 Write a Python program to check whether a string contains all letters of the alphabet.
s = input('Enter the string : ')
lower =set([chr(x) for x in range (65,91)])
upper = set([chr(x) for x in range (97,122)])
alphabet_set= lower | upper 
x = set(s)
print(alphabet_set)
print(x)
print(x & alphabet_set)
if (x & alphabet_set) == alphabet_set:
#     print('All alphabets are present')
# else:
#     print(x-alphabet_set)
