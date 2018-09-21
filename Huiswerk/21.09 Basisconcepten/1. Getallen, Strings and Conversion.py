cijferICOR = float(input('Vul je verwachte cijfer voor ICOR in: '))
cijferPROG = float(input('Vul je verwachte cijfer voor PROG in: '))
cijferCSN = float(input('Vul je verwachte cijfer voor CSN in: '))

gemiddelde = (cijferCSN + cijferICOR + cijferPROG) / 3
beloning = gemiddelde *3 *30

print("Het gemiddelde van je cijfers (wat een %d is) levert je een beloning van €%d op" % (gemiddelde, beloning))