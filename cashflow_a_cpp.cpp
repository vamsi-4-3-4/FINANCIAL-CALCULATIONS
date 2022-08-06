#include<iostream>
using namespace std;
class financial{
public:
float netincrease(float cash_from_operating,float cash_from_finacing,float cash_from_investing){
    return cash_from_operating+cash_from_finacing-cash_from_investing;
}

float cashcurrent(float net_increase,float cash_last_term){
return net_increase+cash_last_term;
}

};
int main(){
    
    
float cash_from_operating,cash_from_investing,cash_from_finacing,cash_last_term,net_increase,cash_current=0;
financial app;
cout<<"ENTER CASH FROM OPERATING:";
cin>>cash_from_operating;
cout<<"ENTER CASH FROM INVESTING:";
cin>>cash_from_investing;
cout<<"ENTER CASH FROM FINANCING:";
cin>>cash_from_finacing;
cout<<"ENTER CASH LAST TERM:";
cin>>cash_last_term;
net_increase=app.netincrease(cash_from_operating,cash_from_finacing,cash_from_investing);
cash_current=app.cashcurrent(net_increase,cash_last_term);
cout<<"YOUR NET INCOME IS:"<<net_increase<<endl;
cout<<"YOUR CURRENT CASH BALANCE IS:"<<cash_current;
}


