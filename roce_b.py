class financial:
    def roce(self,pbit,totalcapitalemployed):
        return pbit/totalcapitalemployed
pbit=float(input("ENTER PBIT:"))
totalcapitalemployed=float(input("ENTER TOTAL CAPITAL EMPLOYED:"))
add=financial()
user=add.roce(pbit,totalcapitalemployed)
print("YOUR ROCE IS ",user*100,"%")