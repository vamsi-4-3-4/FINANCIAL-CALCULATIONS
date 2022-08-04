totalequity=0
equitysharecapital=0
reservesandsurplus=0
preferredequity=0
totaldebt=0
shorttermdebt=0
longtermdebt=0

print("CALCULATING DEBT TO EQUITY RATIO:")
print("PROVIDE THE EQUITY VALUES")
equitysharecapital=float(input("ENTER EQUITY SHARE CAPITAL"))
reservesandsurplus=float(input("ENTER RESERVESAND SURPLUS:"))
preferredequity=float(input("ENTER PREFERRED EQUITY:"))
print("PROVIDE THE DEBT VALUES")
shorttermdebt=float(input("ENTER SHORT TERM DEBT:"))
longtermdebt=float(input("ENTER LONG TERM DEBT:"))


totalequity=equitysharecapital+reservesandsurplus+preferredequity
totaldebt=shorttermdebt+longtermdebt
print("DEBT TO EQUITY RATIO:",totaldebt/totalequity)
