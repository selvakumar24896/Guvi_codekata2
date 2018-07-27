inp=input()
position=[]
flag=0
init=2
if inp>0:
	for x in range(0,3):
		for y in range(0,inp/2):
			if flag%2==0:
				position.append(init)
				init=init+2
			else:
				position.append(init)
				init=init+2
		init=0		
		flag+=1
		init=init+flag

	print len(position)
	print position
else:
	print "Invalid input"




