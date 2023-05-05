from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json
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

    new_data = {
        website: {
            "email": email,
            "password": passw,
        }
    }

    if len(website) == 0 or len(passw) == 0:
        messagebox.showinfo(title="Empty field", message="Fill all fields.")
    else:
        try:
            with open("data.json", mode="r") as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                # Saving updated data
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", mode="w") as file:
                # Saving updated data
                json.dump(new_data, file, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_pass.delete(0, END)


# ----------------------------- Search -------------------------------- #

def search_data():
    # Checking if entry not empty.
    search_name = entry_website.get()
    if len(search_name) == 0:
        messagebox.showinfo(title="Empty window error", message="Website field can't be empty.")
    else:
        try:
            # Opening data file
            with open("data.json", mode="r") as file:
                # Reading old data
                data = json.load(file)
        # If there is no data show infobox
        except FileNotFoundError:
            messagebox.showinfo(title="No file Error", message="No Data File Found")
        else:
            # Check if website is in data file
            if search_name in data:
                search_email = data[search_name]["email"]
                search_pass = data[search_name]["password"]
                messagebox.showinfo(title=search_name, message=f"Email: {search_email} \nPassword: {search_pass}")
            else:
                # If there is no suitable data in file show infobox.
                messagebox.showinfo(title="No data Error", message=f"No data of '{search_name}' website.")


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
entry_website.grid(column=2, row=2, padx=2, pady=2, sticky=W + E)
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

search_btn = Button(text="Search", command=search_data)
search_btn.grid(column=3, row=2, padx=2, pady=2, sticky=W + E)

window.mainloop()
