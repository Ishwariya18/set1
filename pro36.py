a = int(input())
M = [ int(x) for x in input().split()]
a = len(M)
c = 0
for i in range(0,a-2):
    for j in range(i+1, a-1):
        for k in range(j+1, a):
            if M[i] > M[j] > M[k] :
                c += 1
print(c)
