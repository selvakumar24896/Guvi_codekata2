str1=raw_input()
str2=raw_input()
count=0
temp2=0
for x in range(0,len(str1)-1):
	temp=x
	for y in range(0,len(str2)-1):
		print "str1=",str1[x]," str2",str2[y]," count=",count
		if str1[x]==str2[y] and str1[x+1]==str2[y+1]:
			count+=1
			x+=1
		
if count!=0:
	print "Yes"
else:
	print "No"