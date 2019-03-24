import java.io.*;
import java.util.Scanner;
class digits
{
public static void main(String args[])
{
int n,sum=0;
Scanner in=new Scanner(System.in);
n=in.nextLine();

for(int i=1;i<=n;++i)
{
sum+=i;
}
System.out.println("sum="+sum);
}
}
