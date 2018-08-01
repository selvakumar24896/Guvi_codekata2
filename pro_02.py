n=input()
k=input()
n=str(n)
li=[]
for i in n:
	li.append(int(i))
	
while k>0:
	temp=min(li)
	ind=li.index(temp)
	if k>=len(li[:ind]) and len(li[:ind])>0:
		li.remove(li[ind-1])
		k-=1
	else:
		li.remove(li[len(li)-1])
		k-=1
result=''
for i in li:
	result+=str(i)
print result