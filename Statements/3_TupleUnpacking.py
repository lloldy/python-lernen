koordinaten = [(1,2), {234, 678}, (23, 45678)]
for ort in koordinaten:
    print(ort)

koordinaten2 = [(1,2), {234, 678}, (23, 45678)]
for x, y in koordinaten:
    print(x, y)

person = {
    "name": "Lara",
    "alter": 22, 
    "beruf": "Data Engineer"
    
}

print(person.keys)  # printet alle keys im dictonarie. Geht auch mit values 

for key in person.keys():
    print(key)