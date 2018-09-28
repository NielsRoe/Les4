leeftijd = int(input("Hoe oud ben je?: "))
paspoort = (input("Heb je een Nederlands paspoort? Ja/Nee:"))

if (leeftijd > 18 or leeftijd == 18) and (paspoort == "Ja"):
    print("Gefeliciteerd, je mag stemmen!")
else:
    print("Helaas, je mag niet stemmen.")