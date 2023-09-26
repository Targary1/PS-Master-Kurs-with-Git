# Task 1
#firstname = (input("Bitte Vornamen eingeben: "))
#surname = input("Bitte Nachnamen eingeben: ")
#age = int(input("Bitte Alter eingeben: "))

#print(f'Die Person heißt {firstname} {surname} und ist {age} Jahre alt.')

# Task 2
first_names = ["Max", "Fritz", "Anna"]
sur_names = ["Mustermann", "Huber", "Neumann"]
command = int(input(f'Bitte wählen sie die 0, 1 oder 2 für den 1. 2. oder 3. Namen: '))

if command == 0:
    print(f'{first_names[0]} {sur_names[0]}')
elif command == 1:
    print(f'{first_names[1]} {sur_names[1]}')
elif command == 2:
    print(f'{first_names[2]} {sur_names[2]}')

# Alternative
print(first_names[command] + " " + sur_names[command])


