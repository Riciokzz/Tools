import tkinter as tk

calculation = ""


def add_calculation(symbol):
    pass


def eval_calculation():
    pass


def clear_field():
    pass


# Calculator window setup

win = tk.Tk()
win.geometry("300x275")
win.title("Calculator")

# Display frame
text_result = tk.Text(win, height=2, width=16, font=("Arial", 24, "bold"))
text_result.grid(columnspan=5)
text_result.pack()

# Buttons frame

win.mainloop()
