daten = "Melinda,Katalin,Siklodi,18"
einzeldaten =daten.split(",")
print(einzeldaten)

daten = "Melinda,Katalin,Siklodi,18"
einzeldaten =daten.split()
print(einzeldaten)

daten = "Melinda,Katalin,Siklodi,18"
einzeldaten =daten.split(",",1)
print(einzeldaten)

inhalte = "Anzahl Wörter in einem Text zählen!"
woerter = inhalte.split()
print("Anzahl der Wörter:",len(woerter))

inhalte = "Morgen ist ein neuer Python Tag!"
woerter = inhalte.split()
print("Heutzutage sind:", len(woerter))

inhalte = "Heute ist ein schöner Tag!"
woerter = inhalte.split()
print("Heute ist:", len(woerter))

inhalte = "Der Text-Editor IDLE unterstützt uns beim Lernen von Python"
woerter = inhalte.split()
print(woerter)
print ("Der Text-Editor:", len(woerter))

inhalte = "Der Text Editor IDLE unterstützt uns beim Lernen von Python"
woerter = inhalte.split()
print(woerter)
print ("Der Text Editor:", len(woerter))



