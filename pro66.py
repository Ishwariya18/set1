a, b, c, d = map(int,input().split())
count = 0
b1 = b-c
if(b1 >= 0):
   di = (a-c)*2
   for i in range(d):
        if(i == d-1):
            di = di/2
        if (b1 < di):
            b1 = a
            count +=1
        b1 = b1 - di
        if (b1 < 0):
            count = -1
            break
        di = 2*a - di
   print(count)
else:
    print(-1)
