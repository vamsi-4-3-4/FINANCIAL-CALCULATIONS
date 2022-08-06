
class financial:
    def netincrease(self,cash_from_operating,cash_from_finacing,cash_from_investing):
        return cash_from_operating+cash_from_finacing-cash_from_investing
    def cashcurrent(self,net_increase,cash_last_term):
        return net_increase+cash_last_term

cash_from_operating=float(input("ENTER CASH FROM OPERATING ACTIVITIES:"))
cash_from_investing=float(input("ENTER CASH FROM INVESTING ACTVITIES:"))
cash_from_finacing=float(input("ENTER CASH FROM FINANCING ACTIVITIES:"))

app=financial()

net_increase=app.netincrease(cash_from_operating,cash_from_finacing,cash_from_investing)

cash_last_term=float(input("ENTER YOUR LAST TERM CASH EXAMPLE LAST YEAR:"))


cash_current=app.cashcurrent(net_increase,cash_last_term)

print("YOUR NET INCOME IS:",net_increase)
print("YOUR CURRENT CASH BALANCE IS:",cash_current)
