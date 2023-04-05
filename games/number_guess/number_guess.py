import random

cpu_number = random.randint(1, 10)
count = 3


game = True
print("Number guessing game.")
while game:
    if count == 0:
        print("You lost!")
        play = input("Do you want to play again? Y/N ")
        if play == "Y":
            count = 3
            cpu_number = random.randint(1, 10)
        else:
            game = False
    elif count > 0:
        user_pick = int(input("Guess a number: "))
        if cpu_number > user_pick:
            print("Higher")
            count -= 1
        elif cpu_number < user_pick:
            print("Lower")
            count -= 1
        elif count > 0 and cpu_number == user_pick:
            print("You win!")
            play = input("Do you want to play again? Y/N ")
            if play == "Y":
                count = 3
                cpu_number = random.randint(1, 10)
            else:
                game = False

