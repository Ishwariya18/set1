u=input()
v=''
w=[]
for i in u:
    if i not in w:
        v+=i
        w.append(i)
    elif i in w:
        break
print(len(w))
