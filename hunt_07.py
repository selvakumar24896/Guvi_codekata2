n=input()


if n>0:
    inp=[]
    out=[]
    
    for i in range(0,n):
        inp.append(input())
        if inp[i]%2!=0 and i%2==0:
            out.append(inp[i])
        if inp[i]%2==0 and i%2!=0:
            out.append(inp[i])

    print(out)
else:
    print("invalid input")       
