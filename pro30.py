ipt=input()
flag=0
for i in range(1,len(ipt)):
  j=0
  while j<len(ipt) and len(ipt[:j]+ipt[i+j:])==len(ipt)-i:
    n=ipt[:j]+ipt[j+i:]
    if int(n)%8==0:
      flag=1
      print('yes')
      break
    j+=1
  if flag==1:
      break
  else:
      print('no')
