n=input()
k=input()
ai=[]
bi=[]
for x in range(0,n):
	ai.append(input())
for x in range(0,n):
	bi.append(input())
count=0
while k>0:
	for i in range(0,n):
		if bi[i]<ai[i]:
			bi[i]<=0
			while bi[i]<ai[i]:
				if k<=0:
					break
				bi[i]+=1
				k-=1
		if bi[i]>=ai[i]:
			bi[i]-=ai[i]
			if i==n-1:
				count+=1
	
print count