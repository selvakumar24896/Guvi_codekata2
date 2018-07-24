def validate(inp):
	status=0
	for x in range(0,len(inp)-1):
		if inp[x][1]==inp[x+1][0]:
			status+=1
		if x==len(inp)-2:
			if inp[x+1][1]==inp[0][0]:
				status+=1
	if status==4:
		return "Yes"
	else:
		return "NO"

inp=[]
for x in range(0,4):
	point=[]
	for y in range(0,2):
		point.append(input())
	inp.append(point)
print validate(inp)
