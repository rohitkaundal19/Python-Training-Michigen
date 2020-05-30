hrs = input("Enter Hours")
h = float(hrs)
rate =input("Enter Rate")
r = float(rate)

if h<=40:
    Pay = (h*r)
elif h>40:
    bhrs = float(h - 40)
    Pay = ((40*r) + (bhrs*(r*1.5)))
else : print ("Wrong Parameter")
print (Pay)
