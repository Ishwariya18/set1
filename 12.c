#include<stdio.h>
int main()
{
int n,rev=0;
scanf("%d",&n);
while(n!=0)
{
rev=(rev*10)+(n%10);
n/=10;
if(rev==n)
{
printf("yes",n);
}
else
{
printf("no",n);

}
return 0;
}
