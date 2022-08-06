class financial:
    def totalassets(self,cash,other_assets):
        return cash+other_assets
    def totalliabilitiesandequity(self,liabilities,common_stock,retained_earnings):
        return liabilities+common_stock+retained_earnings
        
cash=0
other_assets=0
add=financial()
cash=float(input("ENTER YOUR CASH:"))
other_assets=float(input("ENTER YOUR OTHER ASSETS:"))
total_assets=add.totalassets(cash,other_assets)
liabilities=0
common_stock=0
retained_earnings=0
liabilities=float(input("ENTER YOUR LIABILITIES:"))
common_stock=float(input("ENTER YOUR COMMON STOCKS:"))
retained_earnings=float(input("ENTER YOUR RETAINED EARNINGS:"))
total_liabilities_and_equity=add.totalliabilitiesandequity(liabilities,common_stock,retained_earnings)
print("YOUR TOTAL ASSETS ARE:",total_assets)
print("YOUR TOTAL LIABILITIES AND EQUITY:",total_liabilities_and_equity)
if total_assets==total_liabilities_and_equity:
    print("SHEET IS BALANCED");
else:
    print("SHEET IS NOT BALANCED BY",total_assets-total_liabilities_and_equity)
