#10. Write a Python program to find the list of words that are longer than n from a given list of words.
l = input('Enter the string ').split()
if len(l)!=0:
    le = input('Specify the length of word to fulfil your requirements ')
    for x in l:
        if len(x)>int(le):
            print(x)
else:
    print('List is empty ')
print(l)
