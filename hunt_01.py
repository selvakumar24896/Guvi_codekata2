def check_repeated(inp):
	out=[]
	for i in range(0,len(inp)):
		for j in range(i+1,len(inp)):
			if inp[i]==inp[j]:
				if inp[i] not in out:
					out.append(inp[i])
	print(out)
	
def main():
	n=int(raw_input())
	inp=[]
	for x in range(n):
		inp.append(int(raw_input()))
	check_repeated(inp)
	
if __name__=="__main__":
	main()
