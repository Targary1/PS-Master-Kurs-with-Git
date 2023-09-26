# Generating the playground
field = ["0", "1", "2",
         "3", "4", "5",
         "6", "7", "8"]

run = True


def print_field():
    print(field[0], field[1], field[2], end="\n", sep="|")
    print(field[3], field[4], field[5], end="\n", sep="|")
    print(field[6], field[7], field[8], end="\n", sep="|")


# logic for one game round
def next_move():
    global position
    global run
    while True:
        position = (input(f'Please insert the desired field: '))
        if position == "q":
            run = False
            return 1
        position = int(position)
        if position <= 9 or position >= 1:
            if field[position] == "X" or field[position] == "O":
                print("Field is already occupied, please choose another one: ")
            else:
                return position
        else:
            print(f'Input must be between 1 and 9. Please repeat your input: ')


# implement win query
def check_win():
    # check rows
    if field[0] == field[1] == field[2]:
        return field[0]
    if field[3] == field[4] == field[5]:
        return field[3]
    if field[6] == field[7] == field[8]:
        return field[6]

    # check columns
    if field[0] == field[3] == field[6]:
        return field[0]
    if field[1] == field[4] == field[7]:
        return field[1]
    if field[2] == field[5] == field[8]:
        return field[2]

    # check diagonals
    if field[0] == field[4] == field[8]:
        return field[0]
    if field[2] == field[4] == field[6]:
        return field[2]


def check_draw():
    if field[0] != "1" and field[1] != "1" and field[2] != "2" and field[3] != "3" and field[4] != "4" and field[5] != \
            "5" and field[6] != "6" and field[7] != "7" and field[8] != "8":
        return True


# Game loop erzeugen
y = 1

while run:
    print_field()
    player_move = next_move()
    if y % 2 == 1:
        field[player_move] = "X"
    else:
        field[player_move] = "O"
    y += 1
    winner = check_win()
    if winner:  # if string not empty, condition is set to be True
        print(f'Player {winner} wins!')
        print_field()
        run = False
    if check_draw():
        print(f'Draw!')
        run = False