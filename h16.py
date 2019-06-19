a1,b=map(int,input().split())
c=list(map(int,input().split()))
discs={}
for i in range(len(c)):
    f=[abs(c[i]-b) for i in range(len(l))]
for i in range(len(c)):
    discs[c[i]]=f[i]
del discs[b]
q=sorted(discs.items(),key = lambda x : x[1])
i=0
for d,e in q:
    i=i+1
    print(d,end=" ")
    if(i==3):
        break
