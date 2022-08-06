const incomebeforeincometaxes=(salesrevenue,cost_of_goods,selling_expenses,general_expenses,administrative_expenses,interest_expense)=>{
    return salesrevenue-(cost_of_goods+selling_expenses+general_expenses+administrative_expenses+interest_expense);
}
const netincome=(salesrevenue,total_expenses)=>{
    return salesrevenue-total_expenses;
}
const totalexpenses=(cost_of_goods,selling_expenses,general_expenses,administrative_expenses,interest_expense,income_tax_expense)=>{
    return cost_of_goods+selling_expenses+general_expenses+administrative_expenses+interest_expense+income_tax_expense
}

//WE TAKE THIS VALUES FROM THE FRONT END OR THE API IF WE HAVE USED THE REST APIS

var salesrevenue=275.1
var cost_of_goods=140.8
var selling_expenses=50
var general_expenses=10
var administrative_expenses=17
var interest_expense=17.2
var income_before_income_taxes=0
var income_tax_expense=17.1
var net_income=0

var total_expenses=totalexpenses(cost_of_goods,selling_expenses,general_expenses,administrative_expenses,interest_expense,income_tax_expense)
var net_income=netincome(salesrevenue,total_expenses);
var income_before_income_taxes=incomebeforeincometaxes(salesrevenue,cost_of_goods,selling_expenses,general_expenses,administrative_expenses,interest_expense);

console.log(income_before_income_taxes)
console.log(net_income)


