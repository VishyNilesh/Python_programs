#21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters. 
s =input()
flag = 0
for x in range(0,4):
    if s[x].isupper():
        flag +=1
if flag > 2:
    new_string=s.upper()
print(new_string)