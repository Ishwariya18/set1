a,b=map(int,input().split())
secs=list(map(int,input().split()))
c=0
for i in secs:
  b1=86400-i
  b=b-b1
  c=c+1
  if b<=0:
    break
print(c)
