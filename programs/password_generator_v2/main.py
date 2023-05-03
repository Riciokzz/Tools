from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

entry_email = Entry()
entry_email.grid(column=2, row=3, columnspan=2, padx=2, pady=2, sticky=W+E)

entry_pass = Entry()
entry_pass.grid(column=2, row=4, padx=2, pady=2, sticky=W+E)

# Buttons
button_gen = Button(text="Generate Password")
button_gen.grid(column=3, row=4, padx=2, pady=2, sticky=W+E)

button_add = Button(text="Add",)
button_add.grid(column=2, row=5, columnspan=2, padx=2, pady=2, sticky=W+E)

window.mainloop()
