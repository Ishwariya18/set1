import java.util.Scanner;
class leap_or_not
{
public static void main(String[] args)
{
int year;
System.out.println("enter the year:");
Scanner in=new Scanner(System.in);
year=in.nextInt();
if(year%4==0)
System.out.println("yes");
else
System.out.println("no");
}
}


