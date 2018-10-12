bruin = {'Best', 'Beukenlaan', 'Eindhoven', 'Helmond \'t Hout', 'Helmond', 'Helmond Brouwhuis', 'Deurne'}
groen = {'Best', 'Beukenlaan', 'Eindhoven', 'Geldrop', 'Heeze', 'Weert'}

print('[Stations die voorkomen bij beide trajecten]')
print(bruin.intersection(groen), '\n')

print('[Stations die traject bruin wel heeft groen niet]')
print(bruin.difference(groen), '\n')

print('[Stations die traject groen wel heeft bruin niet]')
print(groen.difference(bruin), '\n')

print('[Alle stations]')
print(bruin.union(groen))