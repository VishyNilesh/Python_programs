# Q. 73  Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string.
s = input ('Enter a string : ')
count_lower = count_upper = count_special = count_numeric = 0 
for x in s:
    if  x.islower():
        count_lower+=1
    elif x.isupper():
        count_upper+=1
    elif x.isnumeric():
        count_numeric+=1
    else : 
        count_special+=1
print('The no. of lowercase characters : ', count_lower)
print('The no. of uppercase characters : ', count_upper)
print('The no. of numeric characters : ', count_numeric)
print('The no. of special characters : ', count_special)