#The formula for future value with compound interest is FV = P(1 + r/n)^nt.
p = float(input("Enter the amount "))
r = float(input("Enter the rate of interest "))
t = float(input("Enter the number of years "))
n = float(input("Enter the number of times the interest is paid every year "))
fv= p*(1+(r*0.01)/n)**(n*t)
print("The future value for the given data is {} ".format(round(fv,2)))
