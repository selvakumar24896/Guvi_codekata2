

def possibility(n,k):
	return n-k

n=input("Total no appartments ")
k=input("inhabited appartments ")
if n>0:
	if k<n:
		print '1',possibility(n,k)
	elif k==n:
		print '0 '*2
	else:
		print "inhabited appartments are greater than Total"
else:
	print"N should not be lessthan 1"
