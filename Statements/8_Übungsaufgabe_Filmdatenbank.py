

Filmdatenbank = {    
"Infinity War": {"Regeseur":"Alberteinstein", "Bewertung": 4.5, "Genre": "Action"},
"Shutter Island" :{"Regeseur": "Lin Long", "Bewertung": 4.3, "Genre": "Drama"},
"Whiplash":{"Regeseur" : "Maik hawk", "Bewerung": 0.3, "Genre": "Musik"},
"Thriller bark movie": {"Regeseur" : "Maik hawk", "Bewerung": 0.3, "Genre": "Thriller"},
"Dark Movie": {"Regeseur" : "Maik hawk", "Bewerung": 0.3, "Genre": "Thriller"}
}


thriller_movies = {titel: daten for titel, daten in Filmdatenbank.items() if "Thriller" in daten.get("Genre")}

print(thriller_movies)

# Dict Comprehension: baut ein neues dict aus einem bestehenden
# {key_ausdruck: value_ausdruck for key, value in ... if bedingung}

# Filmdatenbank.items() -> gibt Paare (key, value) zurück, hier also (titel, daten)
#   titel = z.B. "Infinity War"
#   daten = z.B. {"Regeseur": "Alberteinstein", "Bewertung": 4.5, "Genre": "Action"}

# daten.get("Genre") -> holt den Wert zum Key "Genre" aus dem inneren dict "daten"
#   .get() statt daten["Genre"], weil .get() bei fehlendem Key None zurückgibt
#   statt einen KeyError zu werfen (sicherer, wenn nicht jeder Film ein Genre hat)

# "Thriller" in daten.get("Genre") -> prüft ob der String "Thriller" im Genre-Wert vorkommt

                         