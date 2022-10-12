#Q.11 Check if a set is a subset of another set, using comparison operators and issubset()
print("Check if a set is a subset of another set, using comparison operators and issubset():\n")
setx = {'apple','mango'}
sety = {'mango','orange'}
setz = {'mango'}
l=[]
for x in setx:
    l.append({x})
for y in sety:
    l.append({y})
l.append(setx)
l.append(sety)
l.append({})
print(l)
for y in setx:
    if {y} in l:
        print({y},'is subset of setx')
    else:
        print({y},'is not subset of setx')
for y1 in sety:
    if {y1} in l:
        print({y1},'is subset of sety')
    else:
        print({y1},'is not subset of sety')
