n=input()
k=input()
c=[]
for x in range(0,n):
	c.append(input())

b=input()
totalbill=0
actual_bill_for_anna=0

for x in range(0,n):
	totalbill+=c[x]
	if x!=k:
		actual_bill_for_anna+=c[x]

actual_bill_for_anna=actual_bill_for_anna/2
shared_bill=totalbill/2

if actual_bill_for_anna==b:
	print "Bon Appetit"
else:
	print shared_bill-actual_bill_for_anna
	
