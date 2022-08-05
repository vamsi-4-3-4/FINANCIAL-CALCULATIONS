class financial:
    def quickratio(self,currentassets,inventories,currentliabilities):
        quickratio=(currentassets-inventories)/currentliabilities
        return quickratio
        
        
adds=financial()

demoratio=adds.quickratio(600000000,100000000,900000000)
print("THIS IS A DEMO RATIO",demoratio,"\n")

currentassets=0
inventories=0
currentliabilities=0
currentassets=float(input("ENTER YOUR CURRENT ASSETS:"))
inventories=float(input('ENTER YOUR INVENTORIES:'))
currentliabilities=float(input("ENTER YOUR CURRENT LIABILITIES:"))
users=adds.quickratio(currentassets,inventories,currentliabilities)
print("YOUR QUICK RATIO IS:",users)
