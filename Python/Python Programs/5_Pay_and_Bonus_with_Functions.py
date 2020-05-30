h = input('Please Enter Hours')
r = input('Please Enter Rate')


hour = float(h)
rate = float(r)

def computepay(hr,rt):
  if hr <= 40:
    pay = (hr * rt)
  elif hr > 40:
    pay = ((40*rt) + ((hr - 40) * rt *1.5))
  else :
    print ("Error")
  return pay

print("The Gross Pay is ", computepay(hour,rate))
