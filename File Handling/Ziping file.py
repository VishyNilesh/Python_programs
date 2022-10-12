from zipfile import *
f = ZipFile('Files.zip','w',ZIP_DEFLATED)
f.write('f1.txt')
f.write('f2.txt')
f.write('f3.txt')
f.write('f4.txt')
f.close()
print('All files zipped successfully !')