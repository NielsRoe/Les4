def code(invoerstring):
    return "".join([chr(ord(c) + 3) for c in invoerstring])

Name = input("Voer uw naam in: ")
Beginstation = input("Voer uw beginstation in: ")
Eindstation = input("Voer uw eindbestemming in: ")
print(code("%s%s%s" % (Name, Beginstation, Eindstation)))