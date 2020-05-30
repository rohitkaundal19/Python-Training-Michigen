import re

try:
    filename = input ("Enter The Filename: ")
    fhand = open (filename)

except:
    print ("Invalid File")

result = list()
Sum = 0

for line in fhand:
    line = line.rstrip()

    if re.search('[0-9]+', line):
        words = re.findall('[0-9]+', line)
        result = result + words

    else:
        continue

for i in range(len(result)):

    Sum = Sum + int(result[i])


print ("The Sum is", Sum)
