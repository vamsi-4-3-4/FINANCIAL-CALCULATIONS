#include<stdio.h>
float netincrease(float cash_from_operating,float cash_from_finacing,float cash_from_investing);
float cashcurrent(float net_increase,float cash_last_term);
int main(){
    
    
float cash_from_operating,cash_from_investing,cash_from_finacing,cash_last_term,net_increase,cash_current=0;
printf("ENTER CASH FROM OPERATING:");
scanf("%f",&cash_from_operating);
printf("ENTER CASH FROM INVESTING:");
scanf("%f",&cash_from_investing);
printf("ENTER CASH FROM FINANCING:");
scanf("%f",&cash_from_finacing);
printf("ENTER CASH LAST TERM:");
scanf("%f",&cash_last_term);


net_increase=netincrease(cash_from_operating,cash_from_finacing,cash_from_investing);
cash_current=cashcurrent(net_increase,cash_last_term);
printf("YOUR NET INCOME IS:%f\n",net_increase);
printf("YOUR CURRENT CASH BALANCE IS:%f\n",cash_current);
    
    
    
    
}

float netincrease(float cash_from_operating,float cash_from_finacing,float cash_from_investing){
    return cash_from_operating+cash_from_finacing-cash_from_investing;
}

float cashcurrent(float net_increase,float cash_last_term){
return net_increase+cash_last_term;
}

