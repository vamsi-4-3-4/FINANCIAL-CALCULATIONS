#include<iostream>
using namespace std;
class financial{
    public:
    float quickratio(float currentassets,float inventories,float currentliabilities){
    return (currentassets-inventories)/currentliabilities;
}


};
int main(){
  financial app;
  float result,currentassets,inventories,currentliabilities=0;
  
  cout<<"ENTER YOUR CURRENT ASSETS:";
cin>>currentassets;
cout<<"ENTER YOUR INVENTORIES:";
cin>>inventories;
cout<<"ENTER YOUR CURRENTLIABILITIES:";
cin>>currentliabilities;
result=app.quickratio(currentassets,inventories,currentliabilities);
cout<<"YOUR QUICK RATIO IS:"<<result;
  
  
  
}
