from zipfile import *
f = ZipFile('Files.zip','r')
names = f.namelist()
for x in names:
    print('file name', x)
    o = open(x,'r')
    print(o.read())
    o.close()
    print()