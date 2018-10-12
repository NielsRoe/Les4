def ticker(filename):
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    tickersymbol = {}

    for line in lines:
        info = line.split(":")
        tickersymbol[info[0]] = info[1].rstrip()
    return tickersymbol

tickersymbol = ticker("tickerSymbols.txt")

company = input("Enter the name of the company: ")
print("Ticker symbol: %s\n" % (tickersymbol[company]))

tickersym = input("Enter ticker symbol: ")
companies = tickersymbol.keys()
print("Company name: %s\n" % (tickersym[companies]))

for comp in companies:
    tickersymbol[comp] = tickersymbol[comp]
    if tickersymbol[comp] == tickersym:
        print(comp)
        break