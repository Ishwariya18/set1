n,m=map(int,input().split())
l=[]
g=0
for i in range(n):
  l.append(list(map(int,input().split())))
for i in range(n):
  for j in range(m-1):
    for k in range(j+1,m+1):
      if l[i][j:k]==[l]*len(l[i][j:k]):
        if all(l[p+i][j:k]==[l]*len(l[p+i][j:k]) for p in range(len(l[i][j:k])-1)):
          if len(l[i][j:k])>g:
            g=len(l[i][j:k])
if len(l)==1 and len(l[0])==1 and l[0][0]==1:
  print(1)
for i in range(g):
  print (*[1]*g)
          
