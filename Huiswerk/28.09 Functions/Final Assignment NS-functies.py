#Deel 1: Functie standaardprijs:
def standaardprijs(afstandKM):
    afstand = afstandKM if afstandKM > 0 else afstandKM == 0

    if afstand > 50:
        return 15 + afstand * 0.60
    else:
        return afstand * 0.80

#Deel 2: Functie Ritprijs:
def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs = standaardprijs(afstandKM)

    if weekendrit:
        if leeftijd < 12 or leeftijd > 64:
            return (prijs * 0.65)
        else:
            return (prijs * 0.60)

    else:
        if leeftijd < 12 or leeftijd > 64:
            return (prijs * 0.70)
        else:
            return (prijs)

#Deel 3: Testen:
print("%.2f" % ritprijs(11, True, -1))
print("%.2f" % ritprijs(11, True, 10))
print("%.2f" % ritprijs(11, True, 51))
print("%.2f" % ritprijs(11, False, -1))
print("%.2f" % ritprijs(11, False, 10))
print("%.2f" % ritprijs(11, False, 51))

print(" ")

print("%.2f" % ritprijs(12, True, -1))
print("%.2f" % ritprijs(12, True, 10))
print("%.2f" % ritprijs(12, True, 51))
print("%.2f" % ritprijs(12, False, -1))
print("%.2f" % ritprijs(12, False, 10))
print("%.2f" % ritprijs(12, False, 51))

print(" ")

print("%.2f" % ritprijs(64, True, -1))
print("%.2f" % ritprijs(64, True, 10))
print("%.2f" % ritprijs(64, True, 51))
print("%.2f" % ritprijs(64, False, -1))
print("%.2f" % ritprijs(64, False, 10))
print("%.2f" % ritprijs(64, False, 51))

print(" ")

print("%.2f" % ritprijs(65, True, -1))
print("%.2f" % ritprijs(65, True, 10))
print("%.2f" % ritprijs(65, True, 51))
print("%.2f" % ritprijs(65, False, -1))
print("%.2f" % ritprijs(65, False, 10))
print("%.2f" % ritprijs(65, False, 51))