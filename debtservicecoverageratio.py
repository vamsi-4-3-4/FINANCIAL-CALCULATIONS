class financial:
    def dscr(self,ebitda,totaldebtservice):
        return ebitda/totaldebtservice
add=financial()
demodscr=add.dscr(40000000,14800000)
print("DEMO DEBT SERVICE COVERAGE RATIO:",demodscr)

ebitda=float(input("ENTER YOUR EBITDA:"))
totaldebtservice=float(input("ENTER YOUR TOTAL DEBT SERVICE:"))
user=add.dscr(ebitda,totaldebtservice)
print("YOUR DEBT SERVICE COVERAGE RATIO IS ",user)
