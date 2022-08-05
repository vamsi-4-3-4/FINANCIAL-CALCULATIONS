class financial:
    def roce(self,pbit,longtermdebt):
        return pbit/totalcapitalemployed
pbit=float(input("ENTER PBIT:"))
longtermdebt=float(input("ENTER LONGTERM DEBT:"))
add=financial()
user=add.roce(pbit,longtermdebt)
print("YOUR ROCE IS ",user*100,"%")