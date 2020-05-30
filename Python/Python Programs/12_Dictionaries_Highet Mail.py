try:
    fhand = input("Enter the File name: ")
    file = open(fhand)
except:
    print ("Invalid Filename")
    quit()

def convert(list):
    return tuple(list)

Result = dict()
for line in file:
    if line.startswith("From "):
        line = (line.strip()).split()
        temp = str(line[1:2])
        temp = temp.replace("'",'')
        temp = temp.replace("[","")
        line = temp.replace("]","")
        if line not in Result:
            Result[line] = 1
        else:
            Result[line] = Result[line]+1


bigcount = 0
bigid = 0
for id,count in Result.items():
    if bigcount is None or count > bigcount:
        bigid = id
        bigcount = count

print (bigid,bigcount)
