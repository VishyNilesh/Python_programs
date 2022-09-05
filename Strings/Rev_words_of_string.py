# Q.40 Write a Python program to reverse words in a string. The quick brown fox jumps over the lazy dog. --> dog. lazy the over jumps fox brown quick The 
s = input ('Enter the string : ')
l = s.split()
l.sort(reverse=True)
print(' '.join(l))
