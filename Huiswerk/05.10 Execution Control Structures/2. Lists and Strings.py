num_strings = 10
strings = []
new_strings = []

while num_strings != 0:
    strings.append(input('Vul hier een woord in (%d): ' % num_strings))
    num_strings -= 1

for i in range(len(strings)):
    if len(strings[i]) == 4:
        new_strings.append(strings[i])
print("De nieuw-gemaakte lijst met alle vier-letter strings is: ")
print(new_strings)