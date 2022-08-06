#include<stdio.h>
float endingretainedearnings(float beginning_retained_earnings,float net_income,float dividens);


int main(){
  float beginning_retained_earnings,net_income,dividens=0;
  printf("ENTER BEGINNING RETAINED EARNINGS:");
  scanf("%f",&beginning_retained_earnings);
  
  printf("ENTER NET INCOME:");
  scanf("%f",&net_income);
  printf("ENTER DIVDENS:");
  scanf("%f",&dividens);
  float result=endingretainedearnings(beginning_retained_earnings,net_income,dividens);
  printf("YOUR ENDING RETAINED EARNINGS ARE:%f",result);
}

float endingretainedearnings(float beginning_retained_earnings,float net_income,float dividens){
  return beginning_retained_earnings+net_income-dividens;
}
