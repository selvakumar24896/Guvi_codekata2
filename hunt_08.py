def check(li):
    a=0
    b=0
    out=[]
    
    for x in range(0,len(li)-1):
        for y in range(x+1,len(li)-1):
            a=li[x]
            b=li[y]
            c=a+b
            temp=li[y:]
            
            if c in temp:
                print a,b,c
                
                
            

n=input()
if n>0:
    inp=[]
    out=[]
    for i in range(0,n):
        inp.append(input())
    check(inp)
else:
    print("invalid input")
        
