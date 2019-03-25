public String generateLowestNumber(String S,int K)
{
if(S==null||K>S.length())
{
return "";
}
int add=S.length()-k;
char[] lowwwest=new char[add];
int[] digits=new int[S.length()];
fot(int i=0;i<digits.length;i++)
{
digits[i]=S.charAt(i)='0';
}
int index=0;
int[]closest=new int[S.length()];
clossest[digits.length-1]=-1;
for(int i=digits.length-2;i>=0;i--)
{
int j=i+1;
while(j!=-1 && digits[i]<=digits[j])
{
j=closest[j];
}
closest[i]=j;
}
for(int i=0;i<add;i++)
{
int j=index;
while(j!=-1 && j<=(digits.length-(add-i)))
{
lowest[i]=(char)(digits[j]+(int) '0');
index=j;
j=closest[j];
}
index++;
}
return String.valueOf(lowest);
}
