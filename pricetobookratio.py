class financial:
    def pricetobookratio(self,tangibleassets,liabilities,totalnumberofshares,currentshareprice):
        bookvalue=tangibleassets-liabilities
        print("book value is:",bookvalue)
        bookvalueshare=bookvalue/totalnumberofshares
        print("BOOK VALUE PER SHARE:",bookvalueshare)
        pricetobookratioo=currentshareprice/bookvalueshare
        return pricetobookratioo
add=financial()
demopb=add.pricetobookratio(1000000000,100000000,500000,1500)
print("DEMO PB RATIO:",demopb,"\n")
tangibleassets=float(input("ENTER TANGIBLE ASSETS:"))
liabilities=float(input("ENTER LIABILITIES:"))
totalnumberofshares=int(input("ENTER TOTAL NUMBER OF SHARES:"))
currentshareprice=float(input("ENTER CURRENT SHARE PRICE:"))
users=add.pricetobookratio(tangibleassets,liabilities,totalnumberofshares,currentshareprice)
print("YOUR PB RATIO:",users)