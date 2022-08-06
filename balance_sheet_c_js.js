const totalcurrentassets=(cash,short_term_investments,accounts_receivable,supplies,prepaid_expenses)=>{
    return cash+short_term_investments+accounts_receivable+supplies+prepaid_expenses;
}
const totalcost=(land,buildings,equipment)=>{
    return land+buildings+equipment;
}
const netpropertyequipment=(total_cost,accumulated_depreciation)=>{
return total_cost-accumulated_depreciation
}
const totalassets=(total_current_assets,net_property_equipment,right_to_assets,intangible_assets)=>{
    return total_current_assets+net_property_equipment+right_to_assets+intangible_assets;
}
const totalcurrentliabilities=(accounts_payable,unearned_revenue,wages_payable,utilities_payable,current_lease_liabilities)=>{
    return accounts_payable+unearned_revenue+wages_payable+utilities_payable+current_lease_liabilities
}
const totalliabilities=(total_current_liabilities,notes_payable,long_term_lease_liabilities)=>{
    return total_current_liabilities+notes_payable+long_term_lease_liabilities
}
const totalshareholdersequity=(common_stock_par_value,additional_paid_in_capital,retained_earnings,tresury_stock)=>{
    return common_stock_par_value+additional_paid_in_capital+retained_earnings-tresury_stock
}
const totalliabilitiesandequity=(total_liabilities,total_shareholders_equity)=>{
    return total_liabilities+total_shareholders_equity
}
var cash=481
var short_term_investments=400
var accounts_receivable=81
var supplies=26
var prepaid_expenses=85
var total_current_assets=totalcurrentassets(cash,short_term_investments,accounts_receivable,supplies,prepaid_expenses)
var land=13
var buildings=1811
var equipment=836
var total_cost=totalcost(land,buildings,equipment)
var accumulated_depreciation=1201
var net_property_equipment=netpropertyequipment(total_cost,accumulated_depreciation)
var right_to_assets=2505
var intangible_assets=69
var total_assets=totalassets(total_current_assets,net_property_equipment,right_to_assets,intangible_assets)
var accounts_payable=116
var unearned_revenue=95
var wages_payable=127
var utilities_payable=156
var current_lease_liabilities=173
var total_current_liabilities=totalcurrentliabilities(accounts_payable,unearned_revenue,wages_payable,utilities_payable,current_lease_liabilities)
var notes_payable=77
var long_term_lease_liabilities=2678
var total_liabilities=totalliabilities(total_current_liabilities,notes_payable,long_term_lease_liabilities)
var common_stock_par_value=1
var additional_paid_in_capital=1466
var tresury_stock=2699
var retained_earnings=2916
var total_shareholders_equity=totalshareholdersequity(common_stock_par_value,additional_paid_in_capital,retained_earnings,tresury_stock)
var total_liabilities_and_equity=totalliabilitiesandequity(total_liabilities,total_shareholders_equity)
console.log("ASSETS")
console.log("YOUR TOTAL CURRENT ASSETS ARE:",total_current_assets)
console.log("YOUR PROPERTY AND EQUIPMENT VALUE IS:",total_cost)
console.log("ACCUMULATED DEPRECIATION:",accumulated_depreciation)
console.log("TOTAL ASSETS",total_assets)
console.log("LIABILITIES AND STOCKHOLDER`S EQUITY")
console.log("YOUR TOTAL CURRENT LIABILITIES",total_current_liabilities)
console.log("YOUR TOTAL LIABILITIES",total_liabilities)
console.log("TOTAL SHARE HOLDERS EQUITY",total_shareholders_equity)
console.log("TOTAL LIABILITIES AND SHARE HOLDERS EQUITY",total_liabilities_and_equity)

if(total_assets==total_liabilities_and_equity){
    console.log("SHEET IS BALANCED")
}else{
    console.log("SHEET IS NOT BALANCED")
}
