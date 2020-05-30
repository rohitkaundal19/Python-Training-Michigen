try:
    fhand = input("Enter the Filename: ")
    file = open (fhand)
except:
    print("Invalid file")
    quit()

count = 0
result = list()
bad_chars = ['@']

for line in file:
    if not line.startswith("From:"):
        continue
    else:
        line = line.split()
        temp = str((line[1:2]))
        temp = temp.replace("'",'')
        temp = temp.replace("[","")
        Result = temp.replace("]","")
        print (Result)
        count = count + 1

print ('There were',count,'lines in the file with From as the first word.')
