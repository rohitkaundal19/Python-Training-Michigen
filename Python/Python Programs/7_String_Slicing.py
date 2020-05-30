text = "X-DSPAM-Confidence:    0.8475";
spos = text.find('0')
epos = text.find('5')
final = float((text[spos:epos+1]))
print (final)


x = 'From marquard@uct.ac.za'
print (x[14:17])
