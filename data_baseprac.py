import sqlite3
import re

conn = sqlite3.connect('prac1.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox.txt'
fh = open(fname)
ory=list()
org=list()
hmm=list()
block=[";"]
blockz=[">"]

for line in fh:
    line=line.strip()
    orgz=re.findall('^From (\S+@\S+)',line)
    for each in orgz:
        if each.endswith(tuple(blockz)):
            new=each[:-len(blockz)]
            if new.endswith(tuple(block)):
                newz=new[:-len(block)]
                ory.append(newz)
            else: 
                ory.append(new)
        elif each.endswith(tuple(block)):
            newiz=each[:-len(block)]
            if newiz.endswith(tuple(blockz)):
                newaz=newiz[:-len(blockz)]
                ory.append(newaz)
            else: 
                ory.append(newiz)
        else:
            ory.append(each)
for each in ory:
    email=each.split("@")
    org.append(email[1])

orgg=tuple(org)
for org in orgg:
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) 
                VALUES ( ?, 1 )''', ( org, ) )
    else : 
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', 
            (org, ))
    conn.commit()
    
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print
print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()

