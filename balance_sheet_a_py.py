class financial:
    def totalassets(self,cash,receivables_from_customers,equipment):
        return cash+receivables_from_customers+equipment
    def totalliabilities(self,accounts_payable,salary_payable):
        return accounts_payable+salary_payable
    def totalliabilitiesandequity(self,total_liabilities,total_shareholders_equity):
        return total_liabilities+total_shareholders_equity

app=financial()

cash=0
receivables_from_customers=0
equipment=0
cash=float(input("ENTER YOUR CASH:"))
receivables_from_customers=float(input("ENTER YOUR RECEIVABLES FROM CUSTOMERS:"))
equipment=float(input("ENTER YOUR EQUIPMENT COST:"))

total_assets=app.totalassets(cash,receivables_from_customers,equipment)

accounts_payable=0
salary_payable=0
accounts_payable=float(input("ENTER YOUR ACCOUNTS PAYABLE:"))
salary_payable=float(input("ENTER YOUR SALARY PAYABLE:"))
total_liabilities=app.totalliabilities(accounts_payable,salary_payable)

common_stock=0
retained_earnings=0
common_stock=float(input("ENTER YOUR COMMON STOCK:"))
retained_earnings=float(input("ENTER YOUR RETAINED EARNINGS:"))
total_shareholders_equity=common_stock+retained_earnings

total_liabilities_and_equity=app.totalliabilitiesandequity(total_liabilities,total_shareholders_equity)


print("YOUR TOTAL ASSETS ARE:",total_assets)
print("YOUR TOTAL LIABILITIES ARE:",total_liabilities)
print("SHARE HOLDERS TOTAL EQUITY IS:",total_shareholders_equity)
print("TOTAL LIABILITIES AND STOCK HOLDERS EQUITY IS:",total_liabilities_and_equity)
if total_assets==total_liabilities_and_equity:
    print("SHEET IS BALANCED")
else:
    print("SHEET IS NOT BALANCED")


    
