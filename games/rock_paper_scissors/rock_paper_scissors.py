import random


score_user = 0
score_cpu = 0


def game():
    global score_user
    global score_cpu
    choices = ["Rock", "Paper", "Scissors"]
    print("\nRock, Paper, Scissors")
    print("Pick one")
    user_move = input()
    while user_move not in choices:
        print("Wrong input")
        print("Rock, Paper, Scissors")
        user_move = input()
    if user_move == "Rock":
        print("You pick Rock.")
    elif user_move == "Paper":
        print("You pick Paper.")
    elif user_move == "Scissors":
        print("You pick Scissors.")

    cpu_move = choices[random.randint(0, 2)]
    print(f"CPU pick {cpu_move}")

    if user_move == cpu_move:
        print("It's a Tie")
    elif user_move == choices[0] and cpu_move == choices[1]:
        print("CPU win!")
        score_cpu += 1
    elif user_move == choices[1] and cpu_move == choices[0]:
        print("User win!")
        score_user += 1

    elif user_move == choices[0] and cpu_move == choices[2]:
        print("User win!")
        score_user += 1
    elif user_move == choices[2] and cpu_move == choices[0]:
        print("CPU win!")
        score_cpu += 1

    elif user_move == choices[1] and cpu_move == choices[2]:
        print("CPU win!")
        score_cpu += 1
    elif user_move == choices[2] and cpu_move == choices[1]:
        print("User win!")
        score_user += 1
    print(f"User score: {score_user}    CPU score: {score_cpu}")
    play_again = input("Play again? Y/N")
    global game_on
    if play_again == "Y":
        game_on = True
    else:
        game_on = False


game_on = False
play = input("Play a game? Y/N  ")
if play == "Y":
    game_on = True
    while game_on:
        game()
        print("\n")
