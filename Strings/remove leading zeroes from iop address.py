# Q.63 Write a Python program to remove leading zeros from an IP address. 255.024.01.01 --> 255.24.1.1
s =input("Enter an ip address : ")
print('.'.join([str(int(i)) for i in s.split('.')]))


