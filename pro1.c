#include<stdio.h>
#include<string.h>
int main()
{
char str[100],temp;
int i,j=0;
gets(string);
i=0;
j=strlen(srr)-1;
while(i<j)
{
temp=str[i];
str[i]=str[j];
str[j]=temp;
i++;
j--;
}
printf(str);
return(0);
}
