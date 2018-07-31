n=input()
k=input()
li=[]
out=[]
for x in range(0,n):
	li.append(input())
if k>=n:
	out=li[:]
else:
	for y in range(0,n,k):
		out.append(min(li[y:y+k]))

print max(out)
