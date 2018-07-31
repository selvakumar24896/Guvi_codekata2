def check(inp):
	rev=''
	inp=str(inp)
	rev+=inp[::-1]
	if rev==inp:
		return 1
	else:
		return 0
inp=input()
inp=str(inp)
n=len(inp)
flag=0
for i in range(0,n):
	if check(inp)==1:
		flag=0
		break
	else:
		inp='0'+inp
		flag=1

if flag==1:
	print "no"
else:
	print "yes"