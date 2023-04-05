import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_upper = [x.upper() for x in alphabet]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', ',', '.', '/', ';', ':']


def check():
    with open("password.txt", 'r') as first:
        datafile = first.readlines()
    for line in datafile:
        if url in line:
            print(f"The password for {url} exists.")
            print(line)
            return True
    return False


url = input("Enter website name: ").upper()


with open("password.txt", 'a+') as p:
    if check():
        quit()
    else:
        cont_work = True
        while cont_work:
            pass_a = int(input("How many letters: "))
            while pass_a <= 1:
                pass_a = int(input("How many letters: "))
            pass_n = int(input("How many numbers: "))
            while pass_n < 1:
                pass_n = int(input("How many numbers: "))
            pass_s = int(input("How many symbols: "))
            while pass_s < 1:
                pass_s = int(input("How many symbols: "))

            len_pass = pass_a + pass_n + pass_s
            len_good = input(f"Your password lenght: {len_pass}. Is it good? Y/N ").upper()
            if len_good == 'Y' or len_good == "YES":
                password = []
                for abc in range(pass_a):
                    if len(password) > 0:
                        password.append(random.choice(alphabet))
                    else:
                        password.append(random.choice(alphabet).upper())
                for num in range(pass_n):
                    password.append(random.choice(numbers))
                for sym in range(pass_s):
                    password.append(random.choice(symbols))
                random.shuffle(password)
                password = ''.join(password)
                cont_work = False
            else:
                cont_work = True
        data = {"URL": url, "PASSWORD": password}
        print(data)
        print("File appended with new password")
        p.write(str(data)+'\n')
