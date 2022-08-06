#include<stdio.h>
float netincome(float pretax_income,float income_tax_expense);
float pretaxincome(float sales_revenue,float expenses);

int main(){
    float sales_revenue,expenses,pretax_income,income_tax_expense,net_income=0;
    printf("ENTER YOUR SALES REVENEUE:");
    scanf("%f",&sales_revenue);
    printf("ENTER YOUR EXPENSES:");
    scanf("%f",&expenses);
    printf("ENTER YOUR INCOME TAX EXPENSE:");
    scanf("%f",&income_tax_expense);
    pretax_income=pretaxincome(sales_revenue,expenses);
    net_income=netincome(pretax_income,income_tax_expense);
    printf("%f",net_income);
    
}



float pretaxincome(float sales_revenue,float expenses){
    return sales_revenue-expenses;
};

float netincome(float pretax_income,float income_tax_expense){
    return pretax_income-income_tax_expense;
}
