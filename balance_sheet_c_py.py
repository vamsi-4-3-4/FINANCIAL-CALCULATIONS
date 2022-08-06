
class financial:
    def totalcurrentassets(self,cash,short_term_investments,accounts_receivable,supplies,prepaid_expenses):
        return cash+short_term_investments+accounts_receivable+supplies+prepaid_expenses
    def totalcost(self,land,buildings,equipment):
        return land+buildings+equipment
    def netpropertyequipment(self,total_cost,accumulated_depreciation):
        return total_cost-accumulated_depreciation
    def totalassets(self,total_current_assets,net_property_equipment,right_to_assets,intangible_assets):
        return total_current_assets+net_property_equipment+right_to_assets+intangible_assets
    def totalcurrentliabilities(self,accounts_payable,unearned_revenue,wages_payable,utilities_payable,current_lease_liabilities):
        return accounts_payable+unearned_revenue+wages_payable+utilities_payable+current_lease_liabilities
    def totalliabilities(self,total_current_liabilities,notes_payable,long_term_lease_liabilities):
        return total_current_liabilities+notes_payable+long_term_lease_liabilities
    def totalshareholdersequity(self,common_stock_par_value,additional_paid_in_capital,retained_earnings,tresury_stock):
        return common_stock_par_value+additional_paid_in_capital+retained_earnings-tresury_stock
    def totalliabilitiesandequity(self,total_liabilities,total_shareholders_equity):
        return total_liabilities+total_shareholders_equity
app=financial()

cash=float(input("ENTER YOUR CASH:"))
short_term_investments=float(input("ENTER YOUR SHORT TERM INVESTMENTS:"))
accounts_receivable=float(input("ENTER ACCOUNTS RECEIVABLE:"))
supplies=float(input("ENTER SUPPLIES:"))
prepaid_expenses=float(input("ENTER PREPAID EXPENSES:"))
total_current_assets=app.totalcurrentassets(cash,short_term_investments,accounts_receivable,supplies,prepaid_expenses)
land=float(input("ENTER VALUE OF THE LAND:"))
buildings=float(input("ENTER VALUE OF THE BUILDINGS:"))
equipment=float(input("ENTER THE VALUE OF THE EQUIPMENT:"))
total_cost=app.totalcost(land,buildings,equipment)
accumulated_depreciation=float(input("ACCUMULATED DEPRECIATION:"))
net_property_equipment=app.netpropertyequipment(total_cost,accumulated_depreciation)
right_to_assets=float(input("OPERATING LEASE RIGHT OF USE ASSETS:"))
intangible_assets=float(input("INTANGIBLE ASSETS:"))
total_assets=app.totalassets(total_current_assets,net_property_equipment,right_to_assets,intangible_assets)
accounts_payable=float(input("ACCOUNTS PAYABLE:"))
unearned_revenue=float(input("UNEARNED REVENUE:"))
wages_payable=float(input("WAGES PAYABLE:"))
utilities_payable=float(input("UTILITIES PAYABLE:"))
current_lease_liabilities=float(input("CURRENT LEASE LIABILITIES:"))
total_current_liabilities=app.totalcurrentliabilities(accounts_payable,unearned_revenue,wages_payable,utilities_payable,current_lease_liabilities)
notes_payable=float(input("NOTES PAYABLE:"))
long_term_lease_liabilities=float(input("LONG TERM LEASE LIABILITIES:"))
total_liabilities=app.totalliabilities(total_current_liabilities,notes_payable,long_term_lease_liabilities)
common_stock_par_value=float(input("COMMON STOCK($0.01 PER VALUE):"))
additional_paid_in_capital=float(input("ADDITIONAL PAID IN CAPITAL:"))
tresury_stock=float(input("TREASURY EARNINGS:"))
retained_earnings=float(input("RETAINED EARNINGS:"))
total_shareholders_equity=app.totalshareholdersequity(common_stock_par_value,additional_paid_in_capital,retained_earnings,tresury_stock)
total_liabilities_and_equity=app.totalliabilitiesandequity(total_liabilities,total_shareholders_equity)
print("ASSETS")
print("YOUR TOTAL CURRENT ASSETS ARE:",total_current_assets)
print("YOUR PROPERTY AND EQUIPMENT VALUE IS:",total_cost)
print("ACCUMULATED DEPRECIATION:",accumulated_depreciation)
print("TOTAL ASSETS",total_assets)
print("LIABILITIES AND STOCKHOLDER`S EQUITY")
print("YOUR TOTAL CURRENT LIABILITIES",total_current_liabilities)
print("YOUR TOTAL LIABILITIES",total_liabilities)
print("TOTAL SHARE HOLDERS EQUITY",total_shareholders_equity)
print("TOTAL LIABILITIES AND SHARE HOLDERS EQUITY",total_liabilities_and_equity)

if total_assets==total_liabilities_and_equity:
    print("SHEET IS BALANCED")
else:
    print("SHEET IS NOT BALANCED")
