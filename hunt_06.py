
def check (li):
	rp=None
	for x in range(0,len(li)-1):
		for y in range(x+1,len(li)):
			if li[x]==li[y]:
				rp=li[x]
				
	if rp is None:
		return "UNIQUE"
	else:
		return rp

n = int(raw_input())
li = []
if n>0:
	for x in range(0,n):
		li.append(int(raw_input()))

	print(check(li))
else:
	print("invalid")
	
	
