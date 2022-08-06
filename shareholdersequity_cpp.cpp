#include<iostream>
using namespace std;
class financial{
public:
float endingretainedearnings(float beginning_retained_earnings,float net_income,float dividens){
  return beginning_retained_earnings+net_income-dividens;
}

};
int main(){
  float beginning_retained_earnings,net_income,dividens=0;
  cout<<"ENTER BEGINNING RETAINED EARNINGS:";
  cin>>beginning_retained_earnings;
  cout<<"ENTER NET INCOME:";
  cin>>net_income;
  cout<<"ENTER DIVDENS:";
  cin>>dividens;
  
  financial add;
  float result=add.endingretainedearnings(beginning_retained_earnings,net_income,dividens);
  cout<<"YOUR ENDING RETAINED EARNINGS ARE:"<<result;
}
