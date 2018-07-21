n=input()
li=[]
for x in range(0,n):
    li.append(raw_input())
li='->'.join(li[::-1])
print li
