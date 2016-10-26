
#for website: http://python-data.dr-chuck.net/known_by_Alesha.html 
#Web crawls 8 sites to append each site's 17th link to names list & prints it

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
link = list()
names=list()
n=1
# Retrieve all of the anchor tags
tags = soup('a')

for tag in tags:
    x=tag.get('href', None)
    x=x.encode('utf-8')
    link.append(x)

new_link=link [17]
names.append(link[17])

while n<7:
    new_page = urllib.urlopen(new_link).read()
    soup=BeautifulSoup(new_page)
    tags=soup('a')
    del link[:]
    for tag in tags:
        x=tag.get('href', None)
        link.append(x)
    names.append(link[17])
    new_link=link[17]
    n=n+1
    
print names 
