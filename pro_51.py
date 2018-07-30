n=input()
li=[]
for x in range(0,n):
	li.append(input())
result=[]
flag=0
count=n
for y in range(0,n-1):
	if li[y]>0 and li[y+1]<0:
		for i in range(li[y],li[y+1],-1):
			if count==0:
				break
			result.append(count)
			count-=1
			flag=0
	elif li[y]<0 and li[y+1]>0:
		for i in range(li[y+1],li[y],-1):
			if count==0:
				break
			result.append(count)
			count-=1
			flag=0
	else:
		result.append(1)
		flag=1
		count-=1
	
if flag==1:
	result.append(1)
print result