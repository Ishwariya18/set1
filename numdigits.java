import java.io.*;
class numdigits {
public static void main(String args[])
{
int count=0,num=3452;
while(num!=0)
{
num/=10;
++count;
}
System.out.println("number of digits:"+count);
}
}
