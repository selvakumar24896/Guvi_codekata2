def check_repeated(inp):
	out=[]
	for i in range(0,len(inp)):
		for j in range(i+1,len(inp)):
			if inp[i]==inp[j]:
				out.append(inp[i])
	print(out)
n=int(raw_input())
inp=[]
for x in range(n):
	inp.append(int(raw_input()))
check_repeated(inp)