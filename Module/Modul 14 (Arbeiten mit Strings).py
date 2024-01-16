test_string = "Das ist ein Test"
# print("Test" not in test_string)
print(test_string.endswith("Das"))

names = ["Hendrik", "Thorsten", "Felix"]
print(", ".join(names))

data = " Haus"
data = data.strip()  # Entfernt alle Weißraumzeichen (Leerzeichen, Tab, Zeilenumbruch)


while True:
    password = input("Please insert passwort (Upper and lower cases necessary)!")
    if password.isupper() or password.islower():
        continue
    else:
        print("Password accepted")
        break

#TODO:  Weitere Methoden lower(), upper(), isalpha(), isalnum(), isdecimal()
#TODO:  Noch mehr Methoden split(), join(), strip(), startwith(), endswith()

#test