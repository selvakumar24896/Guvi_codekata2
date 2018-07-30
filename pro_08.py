def gcd(l,r):
	if l==r:
		return r
	if l<r:
		return gcd(l,r-l)
	if r<l:
		return gcd(l-r,r)
	if l==0 or r==0:
		return 0
	 
n=input()
q=input()
li=[]
qli=[]
for x in range(0,n):
	li.append(input())
for y in range(0,q*2):
	qli.append(input())
#print li
#print qli
for i in range(0,q*2,2):
	#print qli[i],"/",qli[i+1]
	print gcd(li[qli[i]-1],li[qli[i+1]-1])