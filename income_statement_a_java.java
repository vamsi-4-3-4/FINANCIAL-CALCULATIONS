import java.util.Scanner;
class financial{
public float netincome(float revenue,float expenses){
return revenue-expenses;
}
}
class Main{
    public static void main(String[] args){
        Scanner s=new Scanner(System.in);
        financial app=new financial();
        float revenue,expenses,mynetincome=0;
    System.out.print("ENTER YOUR REVENUE:");
    revenue=s.nextFloat();
    System.out.print("ENTER YOUR EXPENSES:");
    expenses=s.nextFloat();
    mynetincome=app.netincome(revenue,expenses);
    System.out.print("YOUR NET INCOME IS:"+mynetincome);
        
        
    }
}


    





