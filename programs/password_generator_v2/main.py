from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
               'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
               'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Fill list with values
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    # Shuffle values in list and join to string
    shuffle(password_list)
    password = "".join(password_list)

    # Setting up entry box
    entry_pass.delete(0, END)
    entry_pass.insert(0, password)

    # Copy text to memory
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_inputs():

    website = entry_website.get()
    email = entry_email.get()
    passw = entry_pass.get()

    if len(website) == 0 or len(passw) == 0:
        messagebox.showinfo(title="Empty field", message="Fill all fields.")
    else:
        is_ok = messagebox.askokcancel(title=entry_website.get(),
                                       message=f"These are the details entered: "
                                       f"\nEmail: {email} "
                                       f"\nPassword: {passw} "
                                       f"\nIs it ok to save?")
        if is_ok:
            entry = f"{website} | {email} | {passw}\n"
            with open("data.txt", mode="a") as file:
                file.write(entry)
                entry_website.delete(0, END)
                entry_email.delete(0, END)
                entry_pass.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=2, row=1)

# Labels
label_website = Label(text="Website:")
label_website.grid(column=1, row=2, sticky=W)

label_email = Label(text="Email/Username:")
label_email.grid(column=1, row=3, sticky=W)

label_pass = Label(text="Password:")
label_pass.grid(column=1, row=4, sticky=W)

# Entry
entry_website = Entry()
entry_website.grid(column=2, row=2, columnspan=2, padx=2, pady=2, sticky=W + E)
entry_website.focus()

entry_email = Entry()
entry_email.grid(column=2, row=3, columnspan=2, padx=2, pady=2, sticky=W + E)
entry_email.insert(0, "name.lastname@email.com")

entry_pass = Entry()
entry_pass.grid(column=2, row=4, padx=2, pady=2, sticky=W + E)

# Buttons
button_gen = Button(text="Generate Password", command=password_generator)
button_gen.grid(column=3, row=4, padx=2, pady=2, sticky=W + E)

button_add = Button(text="Add", command=save_inputs)
button_add.grid(column=2, row=5, columnspan=2, padx=2, pady=2, sticky=W + E)

window.mainloop()
