import random

images = ["🚪", "🐐", "🏆"]



# create 3 doors
def shuffle_doors():
    door_list = ["goat", "goat", "prize"]
    random.shuffle(door_list)
    #print(door_list)
    return door_list


# user pick door
def pick_door(doors):
    while True:
        pick = input("Which door you pick? ")
        if pick.isdigit():
            pick = int(pick)
            if 0 < pick < 4:
                if doors.index("prize") == pick - 1:
                    goat_door = random.choice([i for i in range(0, 3) if i != pick - 1])
                else:
                    goat_door = random.choice([i for i in range(0, 3) if i not in [pick - 1, doors.index("prize")]])
                doors_images[goat_door] = images[1]
                print("\nRevealing one door.")
                print(doors_images)
                break
            else:
                print("Enter door number 1 - 3. ")
        else:
            print("It's not a number. ")
    return pick - 1, goat_door


def change_door(user_pick):
    pick_change = input("Do you want to change doors? Y/N ")
    if pick_change.upper() == "Y":
        while True:
            pick = input("Which door you pick? ")
            if pick.isdigit():
                pick = int(pick)
                if 0 < pick < 4:
                    break
                else:
                    print("Enter door number. ")
            else:
                print("It's not a number. ")
        return pick - 1
    else:
        user_pick = user_pick
        return user_pick


def game_over(doors, user_pick, win):
    print("\n")
    doors_images[doors.index("prize")] = images[2]
    doors_images[doors.index("goat")] = images[1]
    print(doors_images)
    if doors[user_pick] == "prize":
        print("You win a prize!")
        win += 1
    else:
        print("You lost, you get a goat.")
        win += 0
    return win


def play_again():
    play = input("Do you want to play again? Y/N ")
    if play.upper() == "Y":
        print("\n")
        return True
    else:
        return False


def game():
    doors = shuffle_doors()
    user_pick, goat_door_1 = pick_door(doors=doors)
    change = change_door(user_pick=user_pick)
    if change != user_pick:
        user_pick = change
    point = game_over(doors=doors, user_pick=user_pick, win=win)
    return point


win = 0
games_played = 0
play = True
while play:
    doors_images = ["🚪", "🚪", "🚪"]
    print("Pick a door.")
    print("1.🚪 | 2.🚪 | 3.🚪")
    games_played += 1
    win = game()
    if games_played > 0 and win > 1:
        print(f"Played times: {games_played}\nWins: {win}\nWinrate: {(win / games_played) * 100}%")
    else:
        print(f"Played times: {games_played}\nLose: {games_played-win}\nWinrate: {(win / games_played) * 100}%")
    if play_again():
        play = True
    else:
        play = False
