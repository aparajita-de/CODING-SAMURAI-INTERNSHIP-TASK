#Project - 1 : Simple Calculator

from tkinter import *

def click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            scvalue.set(eval(scvalue.get()))
        except:
            scvalue.set("Error")

    elif text == "C":
        scvalue.set("")

    else:
        scvalue.set(scvalue.get() + text)


# ---------- Window ----------
root = Tk()
root.title("Simple Calculator by Aparajita De")
root.configure(bg="#1e1e1e")
root.minsize(360, 520)

# ---------- Display ----------
scvalue = StringVar()
screen = Entry(
    root,
    textvariable=scvalue,
    font=("Segoe UI", 26),
    bd=8,
    relief=RIDGE,
    justify=RIGHT
)
screen.grid(row=0, column=0, columnspan=4, padx=10, pady=15, sticky="nsew")

# ---------- Button Creator ----------
def make_button(text, row, col, bg, colspan=1):
    b = Button(
        root,
        text=text,
        font=("Segoe UI", 18),
        bg=bg,
        fg="white",
        relief=RAISED
    )
    b.grid(
        row=row,
        column=col,
        columnspan=colspan,
        padx=5,
        pady=5,
        sticky="nsew"
    )
    b.bind("<Button-1>", click)

# ---------- Buttons ----------
make_button("7", 1, 0, "#3a3a3a")
make_button("8", 1, 1, "#3a3a3a")
make_button("9", 1, 2, "#3a3a3a")
make_button("/", 1, 3, "#1976d2")

make_button("4", 2, 0, "#3a3a3a")
make_button("5", 2, 1, "#3a3a3a")
make_button("6", 2, 2, "#3a3a3a")
make_button("*", 2, 3, "#1976d2")

make_button("1", 3, 0, "#3a3a3a")
make_button("2", 3, 1, "#3a3a3a")
make_button("3", 3, 2, "#3a3a3a")
make_button("-", 3, 3, "#1976d2")

make_button("0", 4, 0, "#3a3a3a")
make_button("00", 4, 1, "#3a3a3a")
make_button("%", 4, 2, "#1976d2")
make_button("+", 4, 3, "#1976d2")

make_button("C", 5, 0, "#d32f2f", colspan=2)
make_button("=", 5, 2, "#388e3c", colspan=2)

# Columns
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Rows 
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
