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