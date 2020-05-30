import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import json

url = input ("Enter location: ")
print ('Retrieving',url)
fhand = urllib.request.urlopen(url).read()
print ('Retrieved',len(fhand),'characters')

file = fhand.decode()

info = json.loads(file)

Sum = 0
count = 0
for item in info['comments']:
    count = count + 1
    Sum = Sum + int(item['count'])

print ('count: ',count)
print ('Sum: ', Sum)
