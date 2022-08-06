import java.util.Scanner;
class financial{
    public float incomebeforeincometaxes(float salesrevenue,float cost_of_goods,float selling_expenses,float general_expenses,float administrative_expenses,float interest_expense){
    return salesrevenue-(cost_of_goods+selling_expenses+general_expenses+administrative_expenses+interest_expense);
}
public float netincome(float salesrevenue,float total_expenses){
    return salesrevenue-total_expenses;
}
public float totalexpenses(float cost_of_goods,float selling_expenses,float general_expenses,float administrative_expenses,float interest_expense,float income_tax_expense){
    return cost_of_goods+selling_expenses+general_expenses+administrative_expenses+interest_expense+income_tax_expense;
}
    
}
class Main{
    public static void main(String[] args){
        Scanner s=new Scanner(System.in);
        
        financial app=new financial();
        float salesrevenue,cost_of_goods,selling_expenses,general_expenses,administrative_expenses,total_expenses=0;
        float interest_expense,income_before_income_taxes,income_tax_expense,net_income=0;
        System.out.print("ENTER YOUR SALES REVENUE:");
salesrevenue=s.nextFloat();
System.out.print("ENTER COST OF GOODS:");
cost_of_goods=s.nextFloat();
System.out.print("ENTER SELLING EXPENSES:");
selling_expenses=s.nextFloat();
System.out.print("ENTER GENERAL EXPENSES:");
general_expenses=s.nextFloat();
System.out.print("ENTER ADMINISTRATIVE EXPENSES:");
administrative_expenses=s.nextFloat();
System.out.print("ENTER INTEREST EXPENSES:");
interest_expense=s.nextFloat();
System.out.print("ENTER INCOME TAX ENPENSES:");
income_tax_expense=s.nextFloat();


total_expenses=app.totalexpenses(cost_of_goods,selling_expenses,general_expenses,administrative_expenses,interest_expense,income_tax_expense);
net_income=app.netincome(salesrevenue,total_expenses);
income_before_income_taxes=app.incomebeforeincometaxes(salesrevenue,cost_of_goods,selling_expenses,general_expenses,administrative_expenses,interest_expense);
System.out.println("INCOME BEFORE INCOME TAXES IS:"+income_before_income_taxes);
System.out.println("NET INCOME IS:"+net_income); 
    }
}



  





