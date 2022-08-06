import java.util.Scanner;
class financial{
    public float pretaxincome(float sales_revenue,float expenses){
    return sales_revenue-expenses;
}

public float netincome(float pretax_income,float income_tax_expense){
    return pretax_income-income_tax_expense;
}

}
class Main{
    public static void main(String[] args){
    Scanner s=new Scanner(System.in);
    financial app=new financial();
    float sales_revenue,expenses,pretax_income,income_tax_expense,net_income=0;
    System.out.print("ENTER YOUR SALES REVENEUE:");
    sales_revenue=s.nextFloat();
    System.out.print("ENTER YOUR EXPENSES:");
    expenses=s.nextFloat();
    System.out.print("ENTER YOUR INCOME TAX EXPENSE:");
    income_tax_expense=s.nextFloat();
    pretax_income=app.pretaxincome(sales_revenue,expenses);
    net_income=app.netincome(pretax_income,income_tax_expense);
    System.out.print("YOUR NET INCOME IS:"+net_income);
    }
}



   





