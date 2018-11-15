import copy


def get(n):
    vl=[]
    for i in range(0,n):
        vl.append(input())
    return vl


def check(l1,l2):
	res=[]
	for i in range(0,len(l1)):
		if l1[i] in l2:
			res.append((l1[i]))
	return res
            
        
li=[]
out=''
a=input()
n=input()


for x in range(0,a):
    li.append(get(n))

out=list(li[0])
for x in range(0,(a-1)):
	out=check(out,li[x+1])
print out
    
