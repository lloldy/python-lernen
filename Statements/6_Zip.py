vornamen = ["Anna", "Laura", "Tom", "Ben"]
nachnamen = ["Schmidt", "Müller", "Van Basten", "Dahm"]
alter = [23, 33 , 21, 27]

for vorname, nachname, a in zip(vornamen, nachnamen, alter):
    print(f"{vorname} {nachname} ist {a} Jahre alt.")