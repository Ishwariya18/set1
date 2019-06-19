a=input()
b=0
c=[]
for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        k=a[i:j+1]
        l=k[::-1]
        if k==l:
            c.append(len(a)-len(l))
print(min(c))
