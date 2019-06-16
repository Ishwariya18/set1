a,b = map(int,input().split())
z = list(map(int,input().split()))
c,d = 0,[]
for i in range(0,len(z)):
  t = i
  for p in range(0,len(z)):
    for l in range(0,b):
      if l == b-1:
        try:
          c += z[p+i]
        except IndexError:
            t = t-1
            c += z[t]
      else:
          c += z[i]
    d.append(c)
    c = 0
 for i in range(0,len(z),b):
   c = sum(z[i:i+b])
   d.append(c)
 print(*sorted(set(c)))
