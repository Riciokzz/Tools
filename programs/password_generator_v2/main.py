from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_inputs():

    website = entry_website.get()
    email = entry_email.get()
    password = entry_pass.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty field", message="Fill all fields.")
    else:
        is_ok = messagebox.askokcancel(title=entry_website.get(),
                                       message=f"These are the details entered: "
                                       f"\nEmail: {email} "
                                       f"\nPassword: {password} "
                                       f"\nIs it ok to save?")
        if is_ok:
            entry = f"{website} | {email} | {password}\n"
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
entry_website.grid(column=2, row=2, columnspan=2, padx=2, pady=2, sticky=W+E)
entry_website.focus()

entry_email = Entry()
entry_email.grid(column=2, row=3, columnspan=2, padx=2, pady=2, sticky=W+E)
entry_email.insert(0, "name.lastname@email.com")

entry_pass = Entry()
entry_pass.grid(column=2, row=4, padx=2, pady=2, sticky=W+E)

# Buttons
button_gen = Button(text="Generate Password")
button_gen.grid(column=3, row=4, padx=2, pady=2, sticky=W+E)

button_add = Button(text="Add", command=save_inputs)
button_add.grid(column=2, row=5, columnspan=2, padx=2, pady=2, sticky=W+E)

window.mainloop()
