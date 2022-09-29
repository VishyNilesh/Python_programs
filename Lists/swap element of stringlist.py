''' Q.3  test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']  o/p : ['efg', 'is', 'bGst', 'for', 'eGGks'] '''
l = ['Gfg', 'is', 'best', 'for', 'Geeks']
l = [x.replace('G','-').replace('e','G').replace('-','e') for x in l]
print(l)