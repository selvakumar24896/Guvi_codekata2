n=input()
m=input()
ni=n
mi=m
out=""
count=0
for x in range(0,n+m):
	if out=='' and mi>0:
		out+='1'
		mi-=1
		count+=1
	elif out[len(out)-2:len(out)]!='11' and mi>0:
		out+='1'
		mi-=1
		count+=1
	elif out[len(out)-1]!='0' and ni>0:
		out+='0'
		ni-=1
		count+=1
if n+m==count:
	print out
else:
	print count-(n+m)
