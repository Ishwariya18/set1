n=int(input())
h=0
globallist=[]
while(h<n):
    lis=list(map(int,input().split(" ")))
    globallist.extend(lis)
    h=h+1
globallist.sort()
h=0
while(h<len(globallist)):
    print(globallist[h],end=" ")
    h=h+1
