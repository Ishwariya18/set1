import util.Scanner;
class one
{
public static void main(String args[])
{
int num;
System.out.println("enter the num");
Scanner in=new Scanner(System.in);
num=in.nextInt();
if(num%2==0)
{
System.out.println("Even");
}
elseif(num%2!=0)
{
System.out.println("Odd");
}
else
{
System.out.println("invalid");
}
}
}






