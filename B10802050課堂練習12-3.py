from tkinter import *

def add():
    n3.set(n1.get() + n2.get())

def subtract():
    n3.set(n1.get() - n2.get())

def multiply():
    n3.set(n1.get() * n2.get())

def divide():
    n3.set(n1.get() / n2.get())

window = Tk()
window.title("ch12.20")

n1 = IntVar()
n2 = IntVar()
n3 = IntVar()

e1 = Entry(window, width=8, textvariable=n1)
label = Label(window, width=3, text='+-*/')
e2 = Entry(window, width=8, textvariable=n2)
btn_add = Button(window, width=5, text='+', command=add)
btn_subtract = Button(window, width=5, text='-', command=subtract)
btn_multiply = Button(window, width=5, text='*', command=multiply)
btn_divide = Button(window, width=5, text='/', command=divide)
e3 = Entry(window, width=8, textvariable=n3)

e1.grid(row=0, column=0)
label.grid(row=0, column=1, padx=5)
e2.grid(row=0, column=2)
btn_add.grid(row=1, column=0, pady=5)
btn_subtract.grid(row=1, column=1, pady=5)
btn_multiply.grid(row=1, column=2, pady=5)
btn_divide.grid(row=1, column=3, pady=5)
e3.grid(row=2, column=1)

window.mainloop()
