''' 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. Go to the editor
Sample String : 'restart'
Expected Result : 'resta$t '''  
s = input("Enter a normal string ")
ch = input("Enter the character you want to replace & get a new string ")
rep = input("Enter the character you want to replace with ")
new_string=""
count = 0
for x in s:
    if x==ch and count<1:
        count+=1
        new_string+=x
    elif x==ch and count>=1:
        x=rep
        new_string+=x
    else:
        new_string+=x
print(new_string)