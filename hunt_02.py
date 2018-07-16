def largenum(inp):
        
	inp=sorted(inp)
	inp.reverse()
	print(inp)
def main():
	n=int(raw_input())
	inp=[]
	for x in range(n):
		inp.append(int(raw_input()))
	largenum(inp)
	
if __name__=="__main__":
	main()
