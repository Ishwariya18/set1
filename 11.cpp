#include<iostream>
#incluse<cmath>
using namespace std;
int main()
{
float base,exponent,result;
cout<<base<<"^"<<exponent<<"=";
while(exponent!=0)
{
result *=base;
--exponent;
}
cout<<result;
return 0;
}

