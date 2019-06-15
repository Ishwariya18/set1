ipt=int(input())
i=0
x=0
b=[]
while i<90 and i<ipt:
  r=0
  for j in str(ipt-i):
    r+=int(j)
  if r+(ipt-i)==ipt:
    x+=1
    b.append(ipt-i)
  i+=1
print(x)
for i in b:
  print(i)
