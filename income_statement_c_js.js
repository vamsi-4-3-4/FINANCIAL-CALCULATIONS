

const pretaxincome=(sales_revenue,expenses)=>{
    return sales_revenue-expenses;
};

const netincome=(pretax_income,income_tax_expense)=>{
    return pretax_income-income_tax_expense;
}



var sales_revenue=117000
var expenses=82000
var income_tax_expense=7000
var pretax_income=pretaxincome(sales_revenue,expenses)
var net_income=netincome(pretax_income,income_tax_expense)
console.log(net_income)

