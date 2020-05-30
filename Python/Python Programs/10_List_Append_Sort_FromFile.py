try :
    fhand = input("Enter the File name : ")
    file = open (fhand)

except :
    print ("Invalid Filename")
    quit()

Result = list()

for line in file:
    word = line.split()
    for i in range(len(word)):
        if word[i] in Result:
            continue
        else:
            Result.append(word[i])

Result.sort()
print (Result)
