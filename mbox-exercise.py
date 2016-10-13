name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

fh = open(name)
collect=dict()


for each in fh:
    if not each.startswith("From:"): continue
    sep=each.split("From: ")
    email=sep[1]
    clean= email.strip()
    collect[clean]=collect.get(clean,0)+1
    

count=0
for each in collect.values():
    if each > count:
        count = each

for key, value in collect.items() :
    if count == value:
        print key, count