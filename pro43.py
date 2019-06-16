t=int(input())
a=list(map(int,input().split()))
s,l=0,[]
b=[x for x in range(1,t+1)]
for i in a:
  if i in b:
      b.remove(i)
k=0
for i in range(0,t-1):
  p=a[i]
  for j in range(i+1,t):
    if p==a[j]:
      if p < b[k]:
        a[j]=b[k]
        s+=1
      else:
        a[i]=b[k]
        s+=1
      k+=1
print(s)
print(*a)
