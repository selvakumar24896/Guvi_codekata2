n=input()
a=input()
b=input()
li1=[]
li2=[]
sum1=0
sum2=0
count=0

while sum1<n and sum2<n:
	li1.append(a)
	li2.append(a)
	sum1+=li1[count]
	sum2+=li2[count]
	count+=1
	li1.append(b)
	li2.append(b)
	sum1+=li1[count]
	sum2+=li2[count]
	count+=1
	
	
if sum1==n and sum2==n:
	print "yes"
else:
	print"No"
	
	
	
