#include<stdio.h>
float incomebeforeincometaxes(float salesrevenue,float cost_of_goods,float selling_expenses,float general_expenses,float administrative_expenses,float interest_expense);
float netincome(float salesrevenue,float total_expenses);
float totalexpenses(float cost_of_goods,float selling_expenses,float general_expenses,float administrative_expenses,float interest_expense,float income_tax_expense);
int main(){
float salesrevenue,cost_of_goods,selling_expenses,general_expenses,administrative_expenses,total_expenses=0;
float interest_expense,income_before_income_taxes,income_tax_expense,net_income=0;
printf("ENTER YOUR SALES REVENUE");
scanf("%f",&salesrevenue);
printf("ENTER COST OF GOODS:");
scanf("%f",&cost_of_goods);
printf("ENTER SELLING EXPENSES:");
scanf("%f",&selling_expenses);
printf("ENTER GENERAL EXPENSES:");
scanf("%f",&general_expenses);
printf("ENTER ADMINISTRATIVE EXPENSES:");
scanf("%f",&administrative_expenses);
printf("ENTER INTEREST EXPENSES:");
scanf("%f",&interest_expense);
printf("ENTER INCOME TAX ENPENSES:");
scanf("%f",&income_tax_expense);


total_expenses=totalexpenses(cost_of_goods,selling_expenses,general_expenses,administrative_expenses,interest_expense,income_tax_expense);
net_income=netincome(salesrevenue,total_expenses);
income_before_income_taxes=incomebeforeincometaxes(salesrevenue,cost_of_goods,selling_expenses,general_expenses,administrative_expenses,interest_expense);
printf("INCOME BEFORE INCOME TAXES IS:%f\n",income_before_income_taxes);
printf("NET INCOME IS:%f",net_income);
    
}
float incomebeforeincometaxes(float salesrevenue,float cost_of_goods,float selling_expenses,float general_expenses,float administrative_expenses,float interest_expense){
    return salesrevenue-(cost_of_goods+selling_expenses+general_expenses+administrative_expenses+interest_expense);
}
float netincome(float salesrevenue,float total_expenses){
    return salesrevenue-total_expenses;
}
float totalexpenses(float cost_of_goods,float selling_expenses,float general_expenses,float administrative_expenses,float interest_expense,float income_tax_expense){
    return cost_of_goods+selling_expenses+general_expenses+administrative_expenses+interest_expense+income_tax_expense;
}



