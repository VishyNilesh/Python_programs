#Q.41  Write a Python program to strip a set of characters from a string. the quick brown fox --> th qck brwn fx

s = input('Enter the string : ')
vowels = ['a','e','i','o','u']
result = ''
for x in s:
    if x.lower() in vowels:
        pass
    else:
        result +=x
print(result)


