import java.util.Scanner;
class financial{
public float endingretainedearnings(float beginning_retained_earnings,float net_income,float dividens){
  return beginning_retained_earnings+net_income-dividens;
}

}


class Main{
    public static void main(String[] args){
        Scanner s=new Scanner(System.in);
        financial add=new financial();
        float result,beginning_retained_earnings,net_income,dividens=0;
        System.out.print("ENTER BEGINNING RETAINED EARNINGS:");
        beginning_retained_earnings=s.nextFloat();
        System.out.print("ENTER NET INCOME:");
        net_income=s.nextFloat();
        System.out.print("ENTER DIVIDENS:");
        dividens=s.nextFloat();
        result=add.endingretainedearnings(beginning_retained_earnings,net_income,dividens);
        System.out.print("YOUR ENDING RETAINED EARNINGS ARE:"+result);
        
    }
}

 
