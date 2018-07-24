inp=raw_input()
out=''
if len(inp)==1:
		out=inp;
else:
	for x in range(0,len(inp)-1):
		if inp[x]!=inp[x+1] and inp[x] not in out:
			out+=inp[x]
		else:
			continue
		if inp[x+1] not in out:
			out+=inp[x+1]

print len(out)
