#include<iostream>
using namespace std;
class financial{
    public:
float netincome(float revenue,float expenses){
return revenue-expenses;
}
    
};
int main(){
    financial app;
    float revenue,expenses,mynetincome=0;
    cout<<"ENTER YOUR REVENUE:";
    cin>>revenue;
    cout<<"ENTER YOUR EXPENSES:";
    cin>>expenses;
    mynetincome=app.netincome(revenue,expenses);
    cout<<"YOUR NET INCOME IS:"<<mynetincome;
    
}





