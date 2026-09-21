#Liste für Schüler
#Dictonarie für Zuordnung der Schüler und ihre Noten

schueler_liste = ["Paula", "Paul", "Max"]
noten_dict = {"Paula": 3.6, "Paul": 3.5, "Max": 2.3}

schueler_liste.append("Lisa")
noten_dict["Lisa"] = 2
schueler_liste.remove("Max")
del noten_dict ["Max"]
noten_dict["Paul"] = 2.7



print(schueler_liste, noten_dict)