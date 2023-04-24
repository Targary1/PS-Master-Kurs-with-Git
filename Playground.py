import numpy as np

number = 9
print(np.sqrt(number))

x = [4, 9, 16, 25]

# Generating new list 1. method
result = []
for item in x:
    new = np.sqrt(item)
    result.append(new)
print(result)

# Generating new list 2. method
result = [np.sqrt(item) for item in x]
print(result)


# while Schleifen

password = 'password123'
user_input = None
counter = 0

while password != user_input and counter < 2:
    if counter == 2:
        break
    user_input = input(f'Please insert your password: ')
    counter += 1

print(f'password correct!')
counter = 0
username = "testuser"
while True:
    name = input(f'Please insert username: ')
    if name != username:
         continue        # Progranmm springt dirket zurück in die Bedingung der while Schleife
    user_input = input(f'Please insert your password: ')
    counter += 1
    if counter < 2:
        if user_input == password:
            break
            print(f'testuser logged in!')
        else: print(f'Try another password.')
    else:
        print(f'Sorry, maximal amount af attempts used.')
        break
