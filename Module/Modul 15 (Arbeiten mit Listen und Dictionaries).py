names = ["Carsten", "Maria", "Friedrich", "Felix", "Carsten"]
names2 = ("Fritz", "Vanessa")
sub_names = names[::2]

names.extend(names2)  # Iterierbare Objekte an Liste anhängen (Liste, Tupel, Strings)

names.reverse()  # in-place Methode, also Methode erzeugt kein neues Objekt, sondern ändert die ursprüngliche Liste

index_carsten = names.index("Carsten", 2, 3)  # fangen nach dem 2. Index an und gehen nur bis zum 3. Index

#TODO: Methoden  append(), insert(), pop(), remove(), index(), extend(), reverse(), sort()

# Löschen auch möglich über Schlüsselwort "del"
del names[2]

#test