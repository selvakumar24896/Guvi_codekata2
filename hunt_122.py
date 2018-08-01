n=input()
li=[]
for x in range(0,n):
	li.append(input())

flag=0
for i in range(0,n):
	lf=0
	rt=0
	for k in range(0,i):
		lf+=li[k]
	for j in range(i+1,n):
		rt+=li[j]
	if lf==rt:
		print "yes"
		flag=1

if flag==0:
	print "No"