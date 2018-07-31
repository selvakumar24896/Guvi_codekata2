def checkshort(vl,track):
	short=track[0]
	if len(track)==1:
		return short
	else:
		for x in range(0,len(track)-1):
			if vl[short][2]<vl[track[x+1]][2]:
				short=short
			else:
				short=track[x+1]
		return short
	
n=input()
m=input()
vl=[]

for x in range(0,m):
	uvw=[]
	for y in range(0,3):
		uvw.append(input())
	vl.append(uvw)

path=[]
for i in range(1,m+1):
	track=[]
	for j in range(0,m):
		if vl[j][0]==i:
			track.append(j)
	if len(track)!=0:
		path.append(checkshort(vl,track))

result=vl[path[0]][2]
start=0
for i in range(0,len(path)-1):
	for  i in range(0,len(path)):
		if start!=i:
			if vl[path[start]][1]==vl[path[i]][0]:
				result+=vl[path[i]][2]
				start=i
if n<=m:
	print result
else:
	print -1*result

