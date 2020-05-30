try:
    fname = input ("Enter the file name :")
except:
    print ("Bad Filename")
    quit()

fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    line = line.upper()
    print (line)
