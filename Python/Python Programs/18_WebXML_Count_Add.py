import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

url = input ("Enter URL: ")
fhand = urllib.request.urlopen(url)
html = fhand.read()
xml = (html.decode())
#print (xml)

Sum  = 0
tree = ET.fromstring(xml)
lst = tree.findall('comments/comment')
print ('Count: ',len(lst))
for item in lst:
    #print (item)
    Sum = Sum + int((item.find('count').text))

print ('Sum: ', Sum)
