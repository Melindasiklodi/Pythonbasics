inhalt = "https://cctrainer.ddnss.de"
ergebnis = inhalt.endswith(".de")
print(ergebnis)

inhalt = "https://cctrainer.ddnss.de"
ergebnis= inhalt.endswith(".de",0,26)
print(ergebnis)

datentyp_tupel= (".de",".com", ".net")

inhalt="http://cctrainer.ddnss.de"
datentyp_tupel=(".de", ".com", ".net")
ergebnis=inhalt.endswith(datentyp_tupel)
print(ergebnis)

inhalt="http://cctrainer.ddnss.de"
ergebnis=inhalt.endswith((".de", ".com", ".net"))
print(ergebnis)
ausgabe = datentyp_tupel ("")
print(ausgabe)
