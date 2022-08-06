import java.util.Scanner;
class financial{
public float netincrease(float cash_from_operating,float cash_from_finacing,float cash_from_investing){
    return cash_from_operating+cash_from_finacing-cash_from_investing;
}

public float cashcurrent(float net_increase,float cash_last_term){
return net_increase+cash_last_term;
}

};
class Main{
    public static void main(String[]args){
float cash_from_operating,cash_from_investing,cash_from_finacing,cash_last_term,net_increase,cash_current=0;
financial app=new financial();
Scanner s=new Scanner(System.in);
System.out.print("ENTER CASH FROM OPERATING:");
cash_from_operating=s.nextFloat();
System.out.print("ENTER CASH FROM INVESTING:");
cash_from_investing=s.nextFloat();
System.out.print("ENTER CASH FROM FINANCING:");
cash_from_finacing=s.nextFloat();
System.out.print("ENTER CASH LAST TERM:");
cash_last_term=s.nextFloat();
net_increase=app.netincrease(cash_from_operating,cash_from_finacing,cash_from_investing);
cash_current=app.cashcurrent(net_increase,cash_last_term);
System.out.println("YOUR NET INCOME IS:"+net_increase);
System.out.println("YOUR CURRENT CASH BALANCE IS:"+cash_current);
    }
}


