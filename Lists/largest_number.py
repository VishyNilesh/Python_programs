#3. Write a Python program to get the largest number from a list.
count = int(input("How many list of number you want to multiply "))
l=[]
largest=0
for i in range(count):
    x = int(input('Enter the number'))
    l.append(x)
    if x >largest:
        largest = x
print('the largest of numbers provided is {}'.format(largest))