#include<iostream>
using namespace std;


class financial{
  public:
  float pretaxincome(float sales_revenue,float expenses){
    return sales_revenue-expenses;
};

float netincome(float pretax_income,float income_tax_expense){
    return pretax_income-income_tax_expense;
}
};


int main(){
      float sales_revenue,expenses,pretax_income,income_tax_expense,net_income=0;
      financial app;
      
    cout<<"ENTER YOUR SALES REVENEUE:";
    cin>>sales_revenue;
    cout<<"ENTER YOUR EXPENSES:";
    cin>>expenses;
    cout<<"ENTER YOUR INCOME TAX EXPENSE:";
    cin>>income_tax_expense;
    pretax_income=app.pretaxincome(sales_revenue,expenses);
    net_income=app.netincome(pretax_income,income_tax_expense);
    cout<<"YOUR NET INCOME IS:"<<net_income;
}

