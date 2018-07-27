t=1;
couter=0
inp=input()
if inp>0:
	while(inp>t):
		t=(t*2)+2

	if inp==t:
		print inp+2
	else:
		t=(t/2)-1
		couter=t+2
		for x in range(t,inp):
			couter-=1
		print couter
else:
	print "Invalid input"

