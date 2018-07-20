def check(li,k):
    li=sorted(li)
    return li[len(li)-k]
    
n=input()
li=[]

if n>0:
    
    k=input()
    if k<=n:
        for x in range(0,n):
            li.append(input())
        print check(li,k)
    else:
        print 'invalid position'
else:
    print 'invalid input'
        
