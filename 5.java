import java.util.Scanner;
public class greatest
{
public static void main(String args[])
{
int a,b,c;
System.out.println("enter the numbers");
Scanner in=new Scanner(System.in);
a=in.nextInt();
b=in.nextInt();
c=in.nextInt();
if(a>b && a>c)
System.out.println(a);
else if(b>a && b>c)
System.out.println(b);
else if(c>a && c>b)
System.out.println(c);
}
}
