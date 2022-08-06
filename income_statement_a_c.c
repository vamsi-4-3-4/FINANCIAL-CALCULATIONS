#include<stdio.h>
float netincome(float revenue,float expenses);

int main(){
    float revenue,expenses,mynetincome=0;
    printf("ENTER YOUR REVENUE:");
    scanf("%f",&revenue);
    printf("ENTER YOUR EXPENSES:");
    scanf("%f",&expenses);
    mynetincome=netincome(revenue,expenses);
    printf("YOUR NET INCOME IS:%f",mynetincome);
}


float netincome(float revenue,float expenses){
return revenue-expenses;
}
