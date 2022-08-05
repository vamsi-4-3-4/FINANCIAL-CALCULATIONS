class financial:
    def roce(self,pbit,equity,longtermdebt,shorttermdebt):
        return pbit/equity+longtermdebt+shorttermdebt
pbit=i=float(intput("ENTER PBIT:"))
equity=float(input("ENTER EQUITY:"))
longtermdebt=float(input("ENTER LONGTERMDEBT:"))
shorttermdebt=float(input("ENTER SHORTTERM DEBT:"))
add=financial()
user=add.roce(pbit,equity,longtermdebt,shorttermdebt)
print("YOUR ROCE IS",user*100,"%")