import os
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog

def browse_folder():
    folder_path = filedialog.askdirectory()
    folder_label.config(text=folder_path)
    return folder_path

def browse_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    file_label.config(text=file_path)
    return file_path

def submit():
    x = float(x_entry.get())
    y = float(y_entry.get())
    r = float(r_entry.get())
    folder_path = folder_label.cget("text")
    file_path = file_label.cget("text")

    all_txt = []
    file_count = 0
    coordinate_count = 0
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_count += 1
            with open(os.path.join(folder_path, filename), 'r') as file:
                for line in file:
                    values = line.strip().split(',')
                    if len(values) >= 4:
                        x_value = float(values[1])
                        y_value = float(values[2])
                        if ((x_value - x) ** 2 + (y_value - y) ** 2) ** 0.5 <= r:
                            all_txt.append(line)
                            coordinate_count += 1

    with open(file_path, 'w') as file:
        file.writelines(all_txt)

    tk.messagebox.showinfo("Atlikta",
                           f"Atlikta be klaidų. Nuskaityti {file_count} .txt failai. Pridėtos {coordinate_count} koordinatės į {file_path}.")


def close_win():
   root.destroy()

root = tk.Tk()
root.title("Taškų paieška v0.2")
root.minsize(300,140)
root.maxsize(300,140)


folder_path = ""

folder_browse_button = tk.Button(root, text="Pasirinkti failus", command=browse_folder, height=1, width=20)
folder_browse_button.grid(row=0, column=0)

folder_label = tk.Label(root, text="Nepasirinkta papkė", height=1, width=20)
folder_label.grid(row=0, column=1)

file_browse_button = tk.Button(root, text="Kur išsaugoti", command=browse_file, height=1, width=20)
file_browse_button.grid(row=1, column=0)

file_label = tk.Label(root, text="Nepasirinktas failas", height=1, width=20)
file_label.grid(row=1, column=1)

x_label = tk.Label(root, text="X Koordinatė:", height=1, width=20)
x_label.grid(row=2, column=0)

x_entry = tk.Entry(root)
x_entry.grid(row=2, column=1)
x_entry.insert(0, "0")

y_label = tk.Label(root, text="Y Koordinatė:", height=1, width=20)
y_label.grid(row=3, column=0)

y_entry = tk.Entry(root)
y_entry.grid(row=3, column=1)
y_entry.insert(0, "0")

r_label = tk.Label(root, text="Atstumas m:", height=1, width=20)
r_label.grid(row=4, column=0)

r_entry = tk.Entry(root)
r_entry.grid(row=4, column=1)
r_entry.insert(0, "0")

submit_button = tk.Button(root, text="Ieškoti", command=submit, height=1, width=20)
submit_button.grid(row=5, column=0)

close_button = tk.Button(root, text="Uždaryti", command=close_win, height=1, width=20)
close_button.grid(row=5, column=1)

root.mainloop()
