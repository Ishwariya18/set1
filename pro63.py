a=input()
b=''
c=[]
for i in a:
    if i not in c:
        b+=i
        c.append(i)
    elif i in c:
        break
print(len(c))
