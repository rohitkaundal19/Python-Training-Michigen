try:
    fhand = input ("Enter the filename: ")
    file = open(fhand)
except:
    print("Invalid File Name")
    quit()

count = dict()
lst = list()
for line in file:
    if line.startswith("From"):
        if line.startswith("From:"):
            continue
        line  = line.split()
        time = str(line[5:6])
        hours = time[2:4]
        #print (hours)
        count[hours] = count.get(hours,0) + 1

count = count.items()
count = sorted(count)
for key,val in count:
    print(key,val)
