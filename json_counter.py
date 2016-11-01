import json
import urllib

url = raw_input('Enter location:')
if len(url) < 1 : url='http://python-data.dr-chuck.net/comments_311996.json'

input = urllib.urlopen(url).read()
info = json.loads(input)

count=0
for each in info['comments']:
    num=each['count']
    count=count+num

print count 
    