n=input()
m=input()

if m>0 and n>0:
    a=[]
    b=[]
    res=[]
    
    for x in range(0,n):
        a.append(input())
    for y in range(0,m):
        b.append(input())

    for y in range(0,m):
        if b[y] in a:
            res.append(b[y])
            a.remove(b[y])
    if b==res:
        print "YES"
    else:
        print "NO"
else:
    print "INVALID INPUT"

        
    
