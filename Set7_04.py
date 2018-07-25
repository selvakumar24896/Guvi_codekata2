

def possibility(n,k):
	return n-k

n=input("Total no appartments ")
k=input("inhabited appartments ")
if n>0:
	if k<=n:
		print possibility(n,k)
	else:
		print "inhabited appartments are greater than Total"
else:
	print"N should not be lessthan 1"
