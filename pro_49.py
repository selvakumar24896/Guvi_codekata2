def divisibility(string,div):
	result=''
	start=0
	stop=len(div)
	for i in range(0,len(string)):
		if string[start:stop]==div:
			result+=string[start:stop]
			start=stop
			stop+=len(div)
	if result==string:
		return 1
	else:
		return 0
str1=raw_input()
str2=raw_input()
temp=""
count=0

for x in range(0,len(str1)):
	temp=str1[:x+1]
	count+=divisibility(str2,temp)
print count