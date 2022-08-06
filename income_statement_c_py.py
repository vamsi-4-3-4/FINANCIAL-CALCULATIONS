class financial:
    def pretaxincome(self,sales_revenue,expenses):
        return sales_revenue-expenses
    def netincome(self,pretax_income,income_tax_expense):
        return pretax_income-income_tax_expense


sales_revenue=0
expenses=0
income_tax_expense=0
sales_revenue=float(input("ENTER YOUR SALES REVENUE:"))
expenses=float(input("ENTER YOUR EXPENSES:"))
income_tax_expense=float(input("ENTER YOUR INCOME TAX EXPENSE:"))

add=financial()

pretax_income=add.pretaxincome(sales_revenue,expenses)
net_income=add.netincome(pretax_income,income_tax_expense)
print("YOUR PRETAX INCOME IS",pretax_income)
print("YOUR NET INCOME IS",net_income)

