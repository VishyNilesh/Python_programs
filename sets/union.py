#Q.8Write a Python program to create a union of sets.
setx = set(["green", "blue"])
sety = set(["blue", "yellow"])
print("Original set elements:")
print(setx)
print(sety)
print("\nIntersection of two said sets:")
setz = setx | sety
ot = setx.union(sety)
print(setz)
print(ot)
