class financial:
    def ending_retained_earnings(self,beginning_retained_earnings,net_income,dividens):
        return beginning_retained_earnings+net_income-dividens

beginning_retained_earnings=0
net_income=0
dividens=0

beginning_retained_earnings=float(input("ENTER BEGINNING RETAINED EARNINGS:"))
net_income=float(input("ENTER NET INCOME:"))
dividens=float(input("ENTER DIVIDENS:"))

add=financial()

endingretainedearnings=add.ending_retained_earnings(beginning_retained_earnings,net_income,dividens)
print("YOUR ENDING RETAINED EARNINGS ARE",endingretainedearnings)
