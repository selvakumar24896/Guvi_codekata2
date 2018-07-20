def check(li,k):
    li=sorted(li)
    while li[len(li)-k] == li[len(li)-(k+1)]:
        print 'in while'
        k=k+1
    print li[len(li)-k]
    
n=input()
li=[]

if n>0:
    k=input()
    if k<=n:
        for x in range(0,n):
            li.append(input())
        check(li,k)
    else:
        print 'invalid position'
else:
    print 'invalid input'
        
