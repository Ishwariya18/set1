import util.Scanner;
class one
{
public static void main(String args[])
{
int x;
System.out.println("enter the value of x:");
Scanner in=new Scanner(System.in);
x=in.nextInt();
if(x%2==0)
{
System.out.println("Even");
}
else if(x%2!=0)
{
System.out.println("Odd");
}
else
{
System.out.println("invalid");
}
}
}






