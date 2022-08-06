const netincrease=(cash_from_operating,cash_from_finacing,cash_from_investing)=>{
    return cash_from_operating+cash_from_finacing-cash_from_investing;
}

const cashcurrent=(net_increase,cash_last_term)=>{
return net_increase+cash_last_term
}

var cash_from_operating=87.5
var cash_from_investing=125.5
var cash_from_finacing=47
var net_increase=netincrease(cash_from_operating,cash_from_finacing,cash_from_investing)
var cash_last_term=1.6
var cash_current=cashcurrent(net_increase,cash_last_term)
console.log("YOUR NET INCOME IS:",net_increase)
console.log("YOUR CURRENT CASH BALANCE IS:",cash_current)
