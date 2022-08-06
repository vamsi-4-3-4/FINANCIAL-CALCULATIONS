#include<iostream>
using namespace std;
class financial{
public:
float incomebeforeincometaxes(float salesrevenue,float cost_of_goods,float selling_expenses,float general_expenses,float administrative_expenses,float interest_expense){
    return salesrevenue-(cost_of_goods+selling_expenses+general_expenses+administrative_expenses+interest_expense);
}
float netincome(float salesrevenue,float total_expenses){
    return salesrevenue-total_expenses;
}
float totalexpenses(float cost_of_goods,float selling_expenses,float general_expenses,float administrative_expenses,float interest_expense,float income_tax_expense){
    return cost_of_goods+selling_expenses+general_expenses+administrative_expenses+interest_expense+income_tax_expense;
}
    
};
int main(){
financial app;
float salesrevenue,cost_of_goods,selling_expenses,general_expenses,administrative_expenses,total_expenses=0;
float interest_expense,income_before_income_taxes,income_tax_expense,net_income=0;
cout<<"ENTER YOUR SALES REVENUE";
cin>>salesrevenue;
cout<<"ENTER COST OF GOODS:";
cin>>cost_of_goods;
cout<<"ENTER SELLING EXPENSES:";
cin>>selling_expenses;
cout<<"ENTER GENERAL EXPENSES:";
cin>>general_expenses;
cout<<"ENTER ADMINISTRATIVE EXPENSES:";
cin>>administrative_expenses;
cout<<"ENTER INTEREST EXPENSES:";
cin>>interest_expense;
cout<<"ENTER INCOME TAX ENPENSES:";
cin>>income_tax_expense;


total_expenses=app.totalexpenses(cost_of_goods,selling_expenses,general_expenses,administrative_expenses,interest_expense,income_tax_expense);
net_income=app.netincome(salesrevenue,total_expenses);
income_before_income_taxes=app.incomebeforeincometaxes(salesrevenue,cost_of_goods,selling_expenses,general_expenses,administrative_expenses,interest_expense);
cout<<"INCOME BEFORE INCOME TAXES IS:"<<income_before_income_taxes;
cout<<"NET INCOME IS:"<<net_income;    
    
}






