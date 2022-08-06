class financial:
    def assets(selt,cash,accountsrecivable,inventories,my_property,plant,equipment):
        return cash+accountsrecivable+inventories+my_property+plant+equipment
    def totalliabilities(self,accounts_payable,notes_payable_to_bank):
        return accounts_payable+notes_payable_to_banks
    def totalshareholdersequity(self,common_stock,retained_earnings):
        return common_stock+retained_earnings
    def liabilitiesandequity(self,total_liabilities,total_share_holders_equity):
        return total_liabilities+total_share_holders_equity
cash=0
accountsrecivable=0
inventories=0
my_property=0
plant=0
equipment=0
cash=float(input("ENTER YOUR CASH:"))
accountsrecivable=float(input("ENTER ACCOUNTSRECIVABLE:"))
inventories=float(input("ENTER INVENTORIES:"))
my_property=float(input("ENTER YOUR PROPERTY:"))
plant=float(input("ENTER PLANTCOST:"))
equipment=float(input("ENTER EQUIPMENT COST:"))
add=financial()
total_assets=add.assets(cash,accountsrecivable,inventories,my_property,plant,equipment)
print("YOUR TOTAL ASSETS ARE",total_assets)
accounts_payable=0
notes_payable_to_banks=0
accounts_payable=float(input("ENTER ACCOUNTS PAYABLES:"))
notes_payable_to_banks=float(input("ENTER NOTES PAYABLE TO BANKS:"))
total_liabilities=add.totalliabilities(accounts_payable,notes_payable_to_banks)
print("YOUR TOTAL LIABILITIES ARE",total_liabilities)
common_stock=0
retained_earnings=0
common_stock=float(input("ENTER COMMON STOCKS AMOUNT:"))
retained_earnings=float(input("ENTER RETAINED EARNINGS:"))
total_share_holders_equity=add.totalshareholdersequity(common_stock,retained_earnings)
print("YOUR TOTAL SHARE HOLDERS EQUITY  IS",total_share_holders_equity)
liabilities_and_equity=add.liabilitiesandequity(total_liabilities,total_share_holders_equity)
print("YOUR LIABILITIES AND SHARE HOLDERS EQUITY IS ",liabilities_and_equity)
print("YOUR TOTAL ASSETS ARE:",total_assets)
if total_assets==liabilities_and_equity:
    print("SHEET WAS BALANCED")
else:
    print("SHEET WAS NOT BALANCED BY ",total_assets-liabilities_and_equity)
