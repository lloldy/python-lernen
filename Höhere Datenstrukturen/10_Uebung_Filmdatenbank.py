Filmdatenbank = {    # dict für anderen dict
"Infinity War": {"Regeseur":"Alberteinstein", "Bewertung": 4.5},  #weiteres dict
"Shutter Island" :{"Regeseur": "Lin Long", "Bewertung": 4.3}, #weiters dict
"Whiplash":{"Regeseur" : "Maik hawk", "Bewerung": 0.3}  #weiters dict
}

Filmdatenbank["The Godfather"] = {"Regeseur": "Lin long", "Bewertung" : 4.5}
Filmdatenbank["Shutter Island"] ["Bewertung"] = 5.0
del Filmdatenbank["Whiplash"]
print(Filmdatenbank)


# : trennt Key von value 
# , trennt mehrere Einträge von einander