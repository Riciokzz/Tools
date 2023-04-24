import tkinter as tk

calculation = ""


def add_calc(n1, n2):
    return n1 + n2


def minus_calc(n1, n2):
    return n1 - n2


def multi_calc(n1, n2):
    return n1 * n2


def divide_calc(n1, n2):
    return n1 / n2


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
