try:
	fname = input ("Enter the filename: ")
except:
	print ("Bad Name of the file")
	quit()

count = 0
result = 0.0
fhand = open(fname)
for line in fhand:
	if not line.startswith('X-DSPAM-Confidence'):
		continue
	count = count + 1
	line = line.lstrip()
	line = line.rstrip()
	spos = line.find(':')
	spam = line [spos+2:]
	spam_value = float(spam)
	result = result + spam_value

print ("Average spam confidence: ",(result/count))
