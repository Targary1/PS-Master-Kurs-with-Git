def gauss(first_name, last_name, title=""):
    print(f'Hallo {title} {first_name} {last_name}')


gauss("Max", "Mustermann", "Dr.")


# Tupel

def generate_passwort(name, age):
    # TODO
    return ("password1", "password2")


generate_passwort("MAX", 12)

password1, password2 = generate_passwort("MAX", 12)  # schnelle Methode zum Entpacken von Tupeln

print(password1)


def multiply(number1, number2, *values):
    product = number1 * number2
    for item in values:
        product *= item
    return product


print(multiply(2, 3, ))

x = lambda a, n: a * n
print(x(3,4), end=", ")

print("test", "user", "debil",sep="\n")

# Globale Variable über Schlüsselwort global definieren
