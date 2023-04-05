import random


def user_move():
    while True:
        inp = int(input("Enter place 1-9: "))
        if grid[inp-1] == "-":
            grid[inp-1] = "X"
            grid_print()
            return False
        else:
            print("Place not valid")


def cpu_move():
    while True:
        move = random.randint(0, 8)
        if grid[move] == "-":
            grid[move] = "O"
            grid_print()
            return False


def grid_print():
    print(f"{grid[0]} | {grid[1]} | {grid[2]}")
    print("---------")
    print(f"{grid[3]} | {grid[4]} | {grid[5]}")
    print("---------")
    print(f"{grid[6]} | {grid[7]} | {grid[8]}")


def check_winner():
    global winner
    if "-" not in grid:
        winner = "TIE"
    elif grid[0] == "X" and grid[1] == "X" and grid[2] == "X":
        winner = "User"
    elif grid[3] == "X" and grid[4] == "X" and grid[5] == "X":
        winner = "User"
    elif grid[6] == "X" and grid[7] == "X" and grid[8] == "X":
        winner = "User"
    elif grid[0] == "X" and grid[3] == "X" and grid[6] == "X":
        winner = "User"
    elif grid[1] == "X" and grid[4] == "X" and grid[7] == "X":
        winner = "User"
    elif grid[2] == "X" and grid[5] == "X" and grid[8] == "X":
        winner = "User"
    elif grid[0] == "X" and grid[4] == "X" and grid[8] == "X":
        winner = "User"
    elif grid[2] == "X" and grid[4] == "X" and grid[6] == "X":
        winner = "User"

    elif grid[0] == "O" and grid[1] == "O" and grid[2] == "O":
        winner = "CPU"
    elif grid[3] == "O" and grid[4] == "O" and grid[5] == "O":
        winner = "CPU"
    elif grid[6] == "O" and grid[7] == "O" and grid[8] == "O":
        winner = "CPU"
    elif grid[0] == "O" and grid[3] == "O" and grid[6] == "O":
        winner = "CPU"
    elif grid[1] == "O" and grid[4] == "O" and grid[7] == "O":
        winner = "CPU"
    elif grid[2] == "O" and grid[5] == "O" and grid[8] == "O":
        winner = "CPU"
    elif grid[0] == "O" and grid[4] == "O" and grid[8] == "O":
        winner = "CPU"
    elif grid[2] == "O" and grid[4] == "O" and grid[6] == "O":
        winner = "CPU"


def play_game():
    print("Tic Tac Toe")
    grid_print()
    print("\n")
    while winner is None:
        print("User move")
        user_move()
        print("\n")
        check_winner()
        if winner == "TIE":
            print("It's a TIE")
            break
        elif winner == "User":
            print(f"Winner is {winner}")

        print("CPU move")
        cpu_move()
        print("\n")
        check_winner()
        if winner == "TIE":
            print("It's a TIE")
            break
        elif winner == "CPU":
            print(f"Winner is {winner}")


play = input("Do you want to play a game? Y/N ").upper()
score_user = 0
score_cpu = 0
if play == "Y":
    while play == "Y":
        grid = ["-", "-", "-",
                "-", "-", "-",
                "-", "-", "-"]
        winner = None
        play_game()

        if winner == "User":
            score_user += 1
        if winner == "CPU":
            score_cpu += 1
        print(f"User score: {score_user}.\n CPU score: {score_cpu}")
        play = input("Do you want to play a game? Y/N ").upper()
