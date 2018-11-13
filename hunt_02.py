def largenum(inp):
        
	inp=sorted(inp)
	inp.reverse()
	print(inp)
n=int(raw_input())

inp=[]


for x in range(n):
	inp.append(int(raw_input()))
largenum(inp)
