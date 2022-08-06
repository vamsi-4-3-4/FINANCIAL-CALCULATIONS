class financial:
    def incomebeforeincometaxes(self,salesrevenue,cost_of_goods,selling_expenses,general_expenses,administrative_expenses,interest_expense):
        return salesrevenue-(cost_of_goods+selling_expenses+general_expenses+administrative_expenses+interest_expense)
    def netincome(self,salesrevenue,total_expenses):
        return salesrevenue-total_expenses
    def totalexpenses(self,cost_of_goods,selling_expenses,general_expenses,administrative_expenses,interest_expense,income_tax_expense):
        return cost_of_goods+selling_expenses+general_expenses+administrative_expenses+interest_expense+income_tax_expense
salesrevenue=0
cost_of_goods=0
selling_expenses=0
general_expenses=0
administrative_expenses=0
interest_expense=0
income_before_income_taxes=0
income_tax_expense=0
net_income=0
salesrevenue=float(input("ENTER SALES REVENUE:"))
cost_of_goods=float(input("ENTER COST OF GOODS:"))
selling_expenses=float(input("ENTER SELLING EXPENSES:"))
general_expenses=float(input("ENTER GENERAL EXPENSES:"))
administrative_expenses=float(input("ENTER ADMINISTRATIVE EXPENSES:"))
interest_expense=float(input("ENTER INTEREST EXPENSES:"))
income_tax_expense=float(input("ENTER INCOME TAX EXPENSE:"))
add=financial()
total_expenses=add.totalexpenses(cost_of_goods,selling_expenses,general_expenses,administrative_expenses,interest_expense,income_tax_expense)
net_income=add.netincome(salesrevenue,total_expenses)
income_before_income_taxes=add.incomebeforeincometaxes(salesrevenue,cost_of_goods,selling_expenses,general_expenses,administrative_expenses,interest_expense)
print("YOUR INCOME BEFOR INCOME TAXES IS",income_before_income_taxes)
print("YOUR NET INCOME IS ",net_income)





