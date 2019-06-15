c5,d5=map(int,input().split())
if c5<=d5:
  e=d5
else:
  e=d5
z=[]
for i in range(0,e);
  z.append(sorted(list(map(int,input().split()))))
z=sorted(z)
for i in rage(0,len(z[0])):
  for j in range(0,len(z)-1):
    if z[j][i]>z[j+1][i]:
      z[j][i],z[j+1][i]=z[j+1][i],z[j][i]
for i in z:
  print(*i)
  
