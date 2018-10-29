f = open("kaartnummers.txt", "r")
lines = f.readlines()
f.close()

for line in lines:
    items = line.split(", ")

    if items[1][-1] == "\n":
        print("{} heeft kaartnummer: {}".format(items[1][0:-1], items[0]))
    else:
        print("{} heeft kaartnummer: {}".format(items[1], items[0]))