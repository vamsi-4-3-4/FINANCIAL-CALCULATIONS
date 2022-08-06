import java.util.Scanner;
class financial{
public float quickratio(float currentassets,float inventories,float currentliabilities){
    return (currentassets-inventories)/currentliabilities;
}
}

class Main{
public static void main(String[]args){
Scanner s=new Scanner(System.in);
financial app=new financial();
float result,currentassets,inventories,currentliabilities=0;
System.out.print("ENTER YOUR CURRENT ASSETS:");
currentassets=s.nextFloat();
System.out.print("ENTER YOUR INVENTORIES:");
inventories=s.nextFloat();
System.out.print("ENTER YOUR CURRENTLIABILITIES:");
currentliabilities=s.nextFloat();
result=app.quickratio(currentassets,inventories,currentliabilities);
System.out.print("YOUR QUICK RATIO IS:"+result);
    }
}
