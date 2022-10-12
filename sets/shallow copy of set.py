#Q.11. Write a Python program to create a shallow copy of sets
setp = set(["Red", "Green"])
setq = set(["Green", "Red"])
#A shallow copy
setr = setp.copy()
print(setr)
