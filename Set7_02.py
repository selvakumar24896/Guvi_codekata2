def check(inp):
	rev=''
	for x in range(len(inp)-1,-1,-1):
		rev+=inp[x]
	if rev==inp:
		return 0

inp=raw_input()
temp=inp
i=0
dummy=None

while i<len(temp)-1:
	res=check(temp[i:len(temp)]);
	if res==0:
		dummy=temp.replace(temp[i:len(temp)],'')
		break
	i+=1

if dummy is None:
	temp=inp
else:
	temp=dummy


i=len(temp)
while i>(len(temp))-2:
	res=check(temp[0:i]);
	if res==0:
		dummy=temp.replace(temp[0:i],'')
		break
	i-=1
	
if dummy is None:
	print len(inp)
else:
	print len(dummy)