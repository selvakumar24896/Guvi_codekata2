li=[]
n=input()
k=input()

for x in range(0,n):
	li.append(input())
	if k==li[x]:
		ind=x
out=[]
l1=0
l2=0


for i in range(1,len(li)):
	if ind-i  >= 0:
		out.append(li[ind-i])
	if ind+i < (len(li)):
		out.append(li[ind+i])

out=sorted(out)
print out[:3]


