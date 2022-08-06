#include<stdio.h>
float quickratio(float currentassets,float inventories,float currentliabilities);
int main(){
float result,currentassets,inventories,currentliabilities=0;
printf("ENTER YOUR CURRENT ASSETS:");
scanf("%f",&currentassets);
printf("ENTER YOUR INVENTORIES:");
scanf("%f",&inventories);
printf("ENTER YOUR CURRENTLIABILITIES:");
scanf("%f",&currentliabilities);
result=quickratio(currentassets,inventories,currentliabilities);
printf("YOUR QUICK RATIO IS:%f",result);

}

float quickratio(float currentassets,float inventories,float currentliabilities){
    return (currentassets-inventories)/currentliabilities;
}


//currentassets=600000000;
//inventories=100000000;
//currentliabilities=900000000;

