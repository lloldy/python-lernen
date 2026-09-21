text = "a"

print(text,text*5)

text2 = "b"*5
print(text2*5)

VORNAME = "Bruno"
NACHNAME = "Roos"

uppercase_name = VORNAME.upper()

print(VORNAME + " " + NACHNAME)

print(VORNAME + " " + uppercase_name)


a = "password"

b = "Password"

# Merke: Es geht nicht darum WELCHE Variable groß-/kleingeschrieben wird,
# sondern dass BEIDE auf dieselbe Schreibweise gebracht werden (hier: beide .upper()).
# Erst dann ist der Vergleich fair - es zählt nur noch, ob dieselben Wörter drinstehen.
if a.upper() == b.upper():
    print("The passwords match.")
else:
    print("The passwords do not match.")


blog_article_title = "Introduction to Python Programming for beginners"
print(blog_article_title.title())