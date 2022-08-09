n1 = int(input("Enter the first positive integer "))
n2 = int(input("Enter the second positive integer "))
i=1
while True:
    x= n1*i
    if x % n2 == 0:
        print("The LCM of {} & {} is {} ".format(n1,n2,x))
        break
    i+=1
