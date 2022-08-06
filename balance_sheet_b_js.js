const totalassets=(cash,other_assets)=>{
    return cash+other_assets;
}
const totalliabilitiesandequity=(liabilities,common_stock,retained_earnings)=>{
    return liabilities+common_stock+retained_earnings
}
var cash=10.6
var other_assets=516.8
var total_assets=totalassets(cash,other_assets)
var liabilities=407.7
var common_stock=55.7
var retained_earnings=64.0
var total_liabilities_and_equity=totalliabilitiesandequity(liabilities,common_stock,retained_earnings)
console.log("YOUR TOTAL ASSETS ARE:",total_assets)
console.log("YOUR TOTAL LIABILITIES AND EQUITY:",total_liabilities_and_equity)
if(total_assets==total_liabilities_and_equity){
    console.log("SHEET IS BALANCED");
}else{
    console.log("SHEET IS NOT BALANCED BY",total_assets-total_liabilities_and_equity)
}
