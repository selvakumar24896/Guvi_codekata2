
def rev(string):
    res=''
    for x in range(len(string)-1,-1,-1):
        res+=string[x]
    return res

st=str(raw_input())
result=''
t=0
for x in range(0,len(st)):  
    if st[x]==' ' or st[x]==st[len(st)-1]:
        result+=rev(st[t:x+1])
        result+=' '
        t=x+1
    
    
print result





