import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup

url = input("Enter URL: ")
count = input("Enter Count: ")
count = int(count)
position = input ("Enter position: ")
position = int (position)


counting = 0
print ("Retrieving: ",url)

while counting < count:
    counting = counting + 1
    fhand = urllib.request.urlopen(url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup ('a')
    pos = 1
    for tag in tags:
        if pos < position:
            pos = pos + 1
            continue
        else:
            result = (tag.get ('href',None))
            print ("Retrieving: ",result)
            break
    url = result
