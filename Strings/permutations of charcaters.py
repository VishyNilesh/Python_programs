#Q.52 Write a Python program to print all permutations with given repetition number of characters of a given string
s = input('Enter a string : ')
l = s.split()
t = []
i = 0
j = 0
temp = 0
while temp < len(s):
    l[i],l[i+1] = l[i+1],l[i]
         

