class financial:
    def interestcoverageratio(self,ebitda,annualinterestpayout):
        return ebitda/annualinterestpayout
add=financial()
demoicr=add.interestcoverageratio(40000000,4800000)
print("DEMO INTEREST COVERAGE RATIO:",demoicr)
ebitda=float(input("ENTER YOUR EBITDA:"))
annualinterestpayout=float(input("ENTER YOUR ANNUAL INTEREST PAYOUT:"))
user=add.interestcoverageratio(ebitda,annualinterestpayout)
print("YOUR ANNAUL INTEREST PAYOUT IS ",user)



