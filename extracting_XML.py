import urllib
from xml.etree import ElementTree as ET

address = raw_input('Enter location:')
if len(address) < 1 : address='http://python-data.dr-chuck.net/comments_311992.xml'

url = (address)
print 'Retrieving', url
uh = urllib.urlopen(url)
tree=ET.parse(uh)
c=tree.findall('comments/comment/count')
sm=list()

for i in c:
    sm.append(i.text)

count=0
for each in sm:
    num=int(each)
    count=count+num

print count

#prompt for url, read xml data
#parse & extract the comment counts 
#compute sums of the counts in the file
