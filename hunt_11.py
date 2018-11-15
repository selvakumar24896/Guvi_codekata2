
def rev(string):
    return string[::-1]+' '


st=raw_input()

result=''
t=0

for x in range(0,len(st)):
    if x==len(st)-1 or st[x+1]==' ':
        temp=st[t:x+1]
        result+=rev(temp.strip())
        t=x+1
      
print result





