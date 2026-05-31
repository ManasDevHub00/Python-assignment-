from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("500x500")

# Global variables
math = ""
i = 0

# Display clicked number
def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))

# Entry box
e = Entry(window, width=56, borderwidth=5)
e.place(x=0, y=0)

# Number buttons
Button(window, text="1", width=12, command=lambda: click(1)).place(x=10, y=60)
Button(window, text="2", width=12, command=lambda: click(2)).place(x=120, y=60)
Button(window, text="3", width=12, command=lambda: click(3)).place(x=230, y=60)

Button(window, text="4", width=12, command=lambda: click(4)).place(x=10, y=120)
Button(window, text="5", width=12, command=lambda: click(5)).place(x=120, y=120)
Button(window, text="6", width=12, command=lambda: click(6)).place(x=230, y=120)

Button(window, text="7", width=12, command=lambda: click(7)).place(x=10, y=180)
Button(window, text="8", width=12, command=lambda: click(8)).place(x=120, y=180)
Button(window, text="9", width=12, command=lambda: click(9)).place(x=230, y=180)

Button(window, text="0", width=12, command=lambda: click(0)).place(x=10, y=240)

# Operations
def add():
    global i, math
    i = int(e.get())
    math = "addition"
    e.delete(0, END)

def sub():
    global i, math
    i = int(e.get())
    math = "subtraction"
    e.delete(0, END)

def mul():
    global i, math
    i = int(e.get())
    math = "multiplication"
    e.delete(0, END)

def div():
    global i, math
    i = int(e.get())
    math = "division"
    e.delete(0, END)

# Equal button
def equal():
    global i, math

    n2 = e.get()

    if not n2:
        return

    n2 = int(n2)
    e.delete(0, END)

    if math == "addition":
        e.insert(0, i + n2)

    elif math == "subtraction":
        e.insert(0, i - n2)

    elif math == "multiplication":
        e.insert(0, i * n2)

    elif math == "division":
        if n2 == 0:
            e.insert(0, "Error")
        else:
            e.insert(0, i / n2)

# Clear button
def clear():
    e.delete(0, END)

# Operator buttons
Button(window, text="+", width=12, command=add).place(x=120, y=240)
Button(window, text="-", width=12, command=sub).place(x=230, y=240)

Button(window, text="*", width=12, command=mul).place(x=10, y=300)
Button(window, text="/", width=12, command=div).place(x=120, y=300)

Button(window, text="=", width=12, command=equal).place(x=230, y=300)

Button(window, text="C", width=12, command=clear).place(x=10, y=360)

window.mainloop()