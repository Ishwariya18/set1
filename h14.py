from itertools import permutations
a=list(input())
b=permutatioms(a)
c=[]
for i in list(b):
    k=''
    for j in i:
        k+=j
    if k not in c:
        c.append(k)
        print(k)
