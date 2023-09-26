# Task 1

for item in range(1, 101):
    if (item % 3 == 0) and (item % 4 == 0):
        print("Zahl ist durch 3 und 4 teilbar")
    elif (item % 4) == 0:
        print("Zahl ist durch 4 teilbar")
    elif (item % 3) == 0:
        print("Zahl ist durch 3 teilbar.")
    else:
        print(item)
#%%

# Task 2 (calculator)

while True:
    value1 = float(input("Bitte erste Zahl eingeben: "))
    value2 = float(input("Bitte zweite Zahl eingeben: "))
    operator = input("Bitte gewünschte Operation eingeben: ")

    if operator == "+":
        print(value1 + value2)
    elif operator == "-":
        print(value1 - value2)
    elif operator == "*":
        print(value1 * value2)
    elif operator == "/":
        print(value1 / value2)

    response = input("Weitere Berechnung vonnöten (Ja oder Nein)? ")

    if response == "Ja":
        continue
    elif response == "Nein":
        break

print("Weiter im Text")

#%%















password = "lion"
user_name = "testuser"
counter = 0
user_input = None


while True:
    name = input(f'Please insert username: ')
    if name != user_name:
        continue
    if counter == 0:
        user_input = input(f'Please insert your password: ')
        if user_input == password:
            print(f'animal has been logged in')
        else:
            counter += 1
            while True:
                user_input = input(f'Try another password: ')
                counter += 1
                if counter <=3:
                    if user_input == password:
                        print(f'animal has been logged in!')
                        break
                else:
                    print(f'Sorry, maximal amount af attempts used.')
                    break
    break
#%%
for item in range(15,10,2):
    print(item)
#%%
