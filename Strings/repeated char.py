#Q.53 Write a Python program to find the first repeated character in a given string.  abcdabcd ---> a

s = input("Enter a string : ")
for x in s:
    if s.count(x)>1:
        print(x)
        break
    else:
        if x == s[-1]:
            print('None')
