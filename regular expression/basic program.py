import re
matcher = re.finditer('ba','abaabaaba')
count = 0
for match in matcher:
    count +=1
    print(match.start(),'---',match.end(),'---',match.group())
print('The count of ocurrence of ba string in target string : ',count)