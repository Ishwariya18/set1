import java.io.*;
import java.util.Scanner;
class digits
{
public static void main(String args[])
{
int num,sum=0;
Scanner in=new Scanner(System.in);
num=in.nextLine();

for(int i=1;i<=num;++i)
{
sum+=i;
}
System.out.println("sum="+sum);
}
}
