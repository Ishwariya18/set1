from operator import xor
from functools import reduce
n,k=map(int,input().split())
l=[int(x) for x in input().split()]
l7=[]
for i in range(k):
  x=[int(x) for x in input().split()]
  l7.append(x)
for i in range(len(17)):
  k=l7[i][0]
  j=l7[i][1]
  x=reduce(xor,l[k-1:j])
  print(x)
