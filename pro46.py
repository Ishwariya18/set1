u=int(input())
v=list(map(int,input().split()))
a=0
b=0
v.sort(reverse=True)
for i in v:
  v=a+i
  if b>s:
    a=s
  else:
    a=b
    b=v
print(a,b)
