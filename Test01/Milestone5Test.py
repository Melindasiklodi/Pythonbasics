daten = "vorname, nachname, alter"
# daten = "vorname; nachname; alter"
# daten = '"vorname";"nachname","alter"'
print (daten)
einzeldaten = daten.split(",")
print(einzeldaten)
einzeldaten = daten.split(", ")
print(einzeldaten)

einzeldaten = daten.split(";")
print(einzeldaten)
ausgabe = daten.split(", ")
print(einzeldaten)
print(ausgabe)

daten = daten.strip(' "  ')
print(daten)
ausgabe = daten.split(' ";" ')
print(ausgabe)
