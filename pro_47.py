n=input()
k=input()
temp=str(n)
temp2='0'*k
val=n
pwr=10
if k>0:
	while 1:
		if temp[len(temp)-k:len(temp)]==temp2 and val%n==0:
			break
		else:
			val=n*pwr
			temp=str(val)
			pwr+=10

print val