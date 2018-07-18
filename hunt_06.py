def check (li):
	rp=None
	p1=None
	p2=None
	for x in range(0,len(li)):
		for y in range(x+1,len(li)):
			if li[x]==li[y]:
				rp=li[x]
	if rp is None:
		return "unique"
	else:
		return rp

n = int(raw_input())
li = []
for x in range(0,n):
	li.append(int(raw_input()))

print(check(li))