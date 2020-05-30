import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup

url = input("Enter URL -")
fhand = urllib.request.urlopen(url)

result = 0
for line in fhand:
    line = str(line)
    #print (line)
    if line.startswith("b'<tr><td>"):
        line = re.findall('[0-9]+', line)
        result = result + int((line[0]))

print (result)
        #print (result)
