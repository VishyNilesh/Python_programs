n1 = int(input("Enter the first positive integer "))
n2 = int(input("Enter the second positive integer "))
list1 = [ i for i in range(1,n1) if n1%i==0 ]
list2 = [ i for i in range(1,n2) if n2%i==0 ]
print("The GCD of {} {} is {}".format(n1,n2,max(set(list1)&set(list2))))