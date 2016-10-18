"""The basic outline of this problem is to read the file, look for integers using the 
re.findall(), looking for a regular expression and then converting the 
extracted strings to integers and summing up the integers.
"""


import re
name = raw_input("Enter file:")
if len(name) < 1 : name = "regex_sampledata.txt"
fhandle = open(name)
numerico=list()

for each in fhandle:
    num=each.strip()
    num = re.findall('[0-9]+',each)
    for each in num:
        item=int(each)
        numerico.append(item)

print sum(numerico)

