x,y=map(int,input().split())
z=list(map(int,input().split()))
z=sorted(z)
t,i=0,0
flag=0
while i<len(z)-2:
  a,b,c=z[i:i+3]
  for j in range(0,y):
    a,b,c=a+1,b+1,c+1
    if a<=5 and b<=5 and c<=5:
      flag=1
    else:
        flag=0
  if flag==1:
    t+=1
  i+=3
  a,b,c=0,0,0
print(t)
