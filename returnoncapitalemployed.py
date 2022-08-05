class financial:
    def roce(self,capitalstructure,capitalemployed):
        return capitalstructure/capitalemployed
add=financial()
demoroce=add.roce(34000000,70000000)
print("DEMO RETURN ON CAPITAL EMPLOYED",demoroce*100,"%")
capitalstructure=float(input("ENTER YOUR CAPITAL STRUCTURE:"))
capitalemployed=float(input("ENTER YOUR CAPITAL EMPLOYED:"))
user=add.roce(capitalstructure,capitalemployed)
print("YOUR RETURN ON CAPITAL EMPLOYED",user*100,"%")

