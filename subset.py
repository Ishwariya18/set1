def isSubset(arr1,arr2,m,n):
i=0
j=0
for i in range(n):
for j in range(m):if(arr2[i]==arr[j]):
break

if(j==m):
return 0
else:
return 1
