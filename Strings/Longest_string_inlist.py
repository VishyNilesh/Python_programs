'''Write a Python function that takes a list of words and return the longest word and the length of the longest one. Go to the editor
Sample Output:
Longest word: Exercises
Length of the longest word: 9 '''
string = input('Enter the list of words separated by space ')
l1 = string.split(' ')
l2 = [len(x) for x in l1]
print(max(l2))
print(l1[l2.index(max(l2))])
