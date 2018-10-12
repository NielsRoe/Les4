students = {
    "Niels": 6.7,
    "Denzell": 7.0,
    "Yorlin": 7.2,
    "Shane": 6.3,
    "Luuk": 8.9,
    "JP": 9.1,
    "Tristan": 9.0,
    "Luthmarnick": 6.3,
}

for name, mark in students.items():
    if mark > 9.0 or mark == 9.0:
        print("%s: %.1f" % (name, mark))