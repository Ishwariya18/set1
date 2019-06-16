u,v=map(int,input().split())
x=list(map(int,input().split()))
if v==1:
    print(min(x))
elif v==2:
    print(max(x[0],x[u-1]))
else:
    print(max(x))
