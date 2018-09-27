score = int(input("Geef je score: "))

if score > 15 or score == 15:
    print("Gefeliciteerd!")
    print("Met een score van %d ben je geslaagd!" % (score))
else:
    print("Helaas, je score is te laag.")