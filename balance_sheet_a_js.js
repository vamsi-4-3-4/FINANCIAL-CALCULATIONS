const totalassets=(cash,receivables_from_customers,equipment)=>{
    return cash+receivables_from_customers+equipment;

}
const totalliabilities=(accounts_payable,salary_payable)=>{
    return accounts_payable+salary_payable;
}
const totalliabilitiesandequity=(total_liabilities,total_shareholders_equity)=>{
 return total_liabilities+total_shareholders_equity
}
var cash=26300
var receivables_from_customers=11800
var equipment=41900

var total_assets=totalassets(cash,receivables_from_customers,equipment)

var accounts_payable=8000
var salary_payable=12000
var total_liabilities=totalliabilities(accounts_payable,salary_payable)

var common_stock=43600
var retained_earnings=16400
var total_shareholders_equity=common_stock+retained_earnings

var total_liabilities_and_equity=totalliabilitiesandequity(total_liabilities,total_shareholders_equity)


console.log("YOUR TOTAL ASSETS ARE:",total_assets)
console.log("YOUR TOTAL LIABILITIES ARE:",total_liabilities)
console.log("SHARE HOLDERS TOTAL EQUITY IS:",total_shareholders_equity)
console.log("TOTAL LIABILITIES AND STOCK HOLDERS EQUITY IS:",total_liabilities_and_equity)
if(total_assets==total_liabilities_and_equity){
    console.log("SHEET IS BALANCED")
}else{
    console.log("SHEET IS NOT BALANCED")
}
