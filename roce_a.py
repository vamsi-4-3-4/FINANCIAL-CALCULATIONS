class financial:
    def roce(self,pbit,equity,noncurrentliabilities):
        return pbit/equity+noncurrentliabilities
add=financial()
pbit=float(input("ENTER PBIT:"))
equity=float(input("ENTER YOUR EQUITY:"))
noncurrentliabilities=float(input("ENTER NON CURRENT LIABILITIES:"))
user=add.roce(pbit,equity,noncurrentliabilities)
print("YOUR ROCE IS",user*100,"%")
