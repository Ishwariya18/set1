nu=int(input())
a=[]
k=bin(2**nu-1)[2::1]
l=len(k)
for i in range(0,2**nu):
    s=bin(i)[2::]
    if len(s)<1:
        a.append([s.count("1"),(1-len(s))*"0"+s])
    else:
        a.append([s.count("1"),s])
a.sort()
for i in range(0,len(a)):
    print(a[i][1])