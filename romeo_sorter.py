
fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()

#remove white space, split, and add to list
for line in fh:
    short=line.rstrip()
    clean=short.split()
    lst.append(clean)

list=lst[1]+lst[0]+lst[2]+lst[3]

for each in list:
    while list.count(each)>1:
        list.remove(each)


list.sort()
print list 