o=open('google1.png','wb')

with(open('google.png','rb')) as f:
	for byte in f:
		o.write(byte)

o.close();