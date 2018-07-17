
def check(li,n):
	count=0
	for i in range(0,len(li)):
		if li[i]==n:
			count+=1
	if count==1:
		print(n)

n=int(raw_input ())
li = []
for x in range (0,n):
	li.append(int(raw_input ()))

for x in range(0,n):
	check(li,x)