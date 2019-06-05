num=int(input())
array=input()
l=list(map(int,array.split(' ')))
min=l[0]
for i in range(1,num):
  if(l[i]<min):
    min=l[i]
print(min)
