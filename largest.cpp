#include<string.h>
#include<vector>
#include<algorithm>
#include<iostream>
using namespace std;
struct {
bool operator()(sring a,string b)
{
string value1=a+b;
string value2=b+a;
return value1>value2;
}
}customCompare;
int main(int argc,char **argv)
{
vector<string>numbers={"10","68","75","7","21","12"};
sort(begin(numbers),end(numbers),customCompare);
for(const auto &elem:numbers){
cout<<elem;
}
cout<<endl;
}
