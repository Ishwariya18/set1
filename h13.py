w=input()
x=len(w)
y=[]
z=""
for i in w:
    y.append(i)
for i in range(x):
    z+=y.pop()
if z==w:
    print('YES')
else:
    print('NO')
