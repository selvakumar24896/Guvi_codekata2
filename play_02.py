def fact(inp):
	if inp==0 or inp ==1:
		return 1
	return inp*fact(inp-1)
inp=input()
print fact(inp)