# Task 1
age = int(input(f'Bitte Geburtsjahr eingeben: '))

print(age <= 2005)

# Alternativ über if-Anweisung
if age <= 2005:
    print(f'Kunde ist 18 Jahre alt')
else:
    print(f'Kunde is noch nicht 18 Jahre alt')

# Task 2
weight = float(input(f'Please insert your weight in kilograms: '))
height = float(input(f'Please insert your height in meters: '))

BMI = weight / (height ** 2)

print(f'Your BMI calculates to: {BMI}')
