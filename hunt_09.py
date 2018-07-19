def check(li):
    for x in range(0,len(li)):
        for y in range(x+1,len(li)):
            if li[x]+li[y]==0:
                return li[x],li[y]
n=input()
li=[]
if n>0:
    for x in range(0,n):
        li.append(input())
    print check(li)
    
else:
    print "invalid input"   
