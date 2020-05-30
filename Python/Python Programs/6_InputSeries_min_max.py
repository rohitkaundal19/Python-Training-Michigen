largest = None
smallest = None

while True:

    Num = input ("Enter The Number : ")
    if Num == 'done':
        break
    try:
        Number = int(Num)
    except:
        print('Invalid input')
        continue
    if largest is None:
        largest = Number
    elif Number > largest:
        largest = Number

    if smallest is None:
        smallest = Number
    elif Number < smallest:
        smallest = Number

print (smallest)
print (largest)
