class financial:
    def netincome(self,revenue,expense):
        return revenue-expense
add=financial()
revenue=float(input("ENTER YOUR REVENUE:"))
expense=float(input("ENTER YOUR EXPENSE:"))
mynetincome=add.netincome(revenue,expense)
print("YOUR NETINCOME IS",mynetincome)
