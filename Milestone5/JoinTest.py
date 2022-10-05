# str = trennzeichen.join(Aufzählung)

wortliste = ['Csipike','Tomi','Andrea']
trennzeichen = '#'
ergebnis = trennzeichen.join(wortliste)
print(ergebnis)

zeichenkette = "abcd"
trennzeichen = '#'
ergebnis = trennzeichen.join(zeichenkette)
print(ergebnis)

wortliste = ['Axel', 'Elke','Martin']
trennzeichen = '#123#'
ergebnis = trennzeichen.join(wortliste)
print(ergebnis)

deutschenglisch = { 'null': 'zero', 'eins': 'one' }
trennzeichen = '#'
print(trennzeichen.join(deutschenglisch))

woerterbuch = { 0: 'null', 1: 'eins'  }
trennzeichen = '#'
print(trennzeichen.join(woerterbuch))
