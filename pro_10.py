n=input()
li=[]
for x in range(0,n):
	li.append(input())
	
res=0
temp2=0

for i in range(0,n):
	temp=li[i]-1
	for j in (0,temp):
		temp2+=j
	res+=temp2
print res

