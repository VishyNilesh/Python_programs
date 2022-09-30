#10. Write a Python program to find the list of words that are longer than n from a given list of words.
''' n=3, "The quick brown fox jumps over the lazy dog" output ['quick', 'brown', 'jumps', 'over', 'lazy']'''
s =input('Enter the string : ')
l = s.split()
n = int(input('Enter the length for words of that length to skip :'))
for x in l:
    if len(x) <4:
        l.remove(x)
print(l)