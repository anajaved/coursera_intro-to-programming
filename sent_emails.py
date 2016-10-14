name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

time=dict()
zzz=list()


for each in handle:
    if not each.startswith("From"): continue
    if each.startswith("From:"): continue
    ind=each.split()
    indz=each.strip()
    pos=indz.find(":")
    hour=indz[pos-2:pos]
    zzz.append(hour)

for ind in zzz:
    time[ind]=time.get(ind,0)+1
    
for k,v in sorted(time.items()):
    print k,v