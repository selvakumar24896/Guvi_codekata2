import sys
def make_equal(inp,extras):
	lt=0
	rt=0
	for x in range(0,len(inp)):
		if '|' not in inp[:x+1]:
			lt+=1
		else:
			rt+=1
	rt-=1
	for y in range(0,len(extras)):
		if lt>rt:
			inp=inp+extras[y]
			rt+=1
		else:
			inp=extras[y]+inp
			lt+=1
	if lt==rt:
		return inp
	else:
		return "Impossible"

inp=raw_input()
inp=inp.upper()
i=0
for x in inp:
	if inp[i] in inp[i+1:]:
		sys.exit("Input has Repeated Weights")
	i+=1
	
i=0
if '|' in inp:
	extras=raw_input()
	extras=extras.upper()
	for x in extras:
		if extras[i] in extras[i+1:] or extras[i] in inp:
			sys.exit("Input has Repeated Weights")
		i+=1
	print make_equal(inp,extras)
else:
	sys.exit("Invalid input")