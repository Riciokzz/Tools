import random


Hidden_Pattern = [['']*8 for x in range(8)]
Guess_Pattern = [['']*8 for x in range(8)]

letter_to_number = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}


def print_board(board):
    print("A B C D E F G H")
    print('***************')
    row_num = 1
    for row in board:
        print("%d|%s|" % (row_num, '|'.join(row)))
        row_num += 1


def get_ship_location():
    column = input("Enter ship column A - H: ").upper()
    while column not in "ABCDEFGH":
        print("Please enter valid column.")
        column = input("Enter ship column A - H: ").upper()
    row = input("Enter ship row 1 - 8: ")
    while row not in "12345678":
        print("Please enter valid row.")
        row = input("Enter ship row 1 - 8: ")
    return int(row)-1, letter_to_number[column]


def create_ships(board):
    for ship in range(5):
        ship_row,ship_column = random.randint(0, 7), random.randint(0, 7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = random.randint(0,7), random.randint(0,7)
        board[ship_row][ship_column] = "X"


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


create_ships(Hidden_Pattern)
print_board(Hidden_Pattern)

turns = 10
while turns > 0:
    print("Battleships\n")
    print_board(Guess_Pattern)
    row,column = get_ship_location()
    if Guess_Pattern[row][column] == "-":
        print("You already guessed that")
    elif Hidden_Pattern[row][column] == "X":
        print("You hit the battleship!")
        Guess_Pattern[row][column] = "X"
        turns -= 1
    else:
        print("Sorry, you missed")
        Guess_Pattern[row][column] = "-"
        turns -= 1
    if count_hit_ships(Guess_Pattern) == 5:
        print("Congratulations you destroyed all the battleships!")
        break
    print(f"You have {turns} turns remaining.")
    if turns == 0:
        print("Game over")
        break