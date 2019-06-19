a1=int(input())
b=[int(x) for x in input().split()]
c=[]
for i in range(0,len(b)):
        k=b[i:]
        l=max(k)
        if b[i]==l:
                c.append(b[i])
print(*c)
print(max(b))
