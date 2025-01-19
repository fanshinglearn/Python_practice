from tkinter import *

with open('課堂練習12-4.txt') as f:
    msg = f.readlines()
    txt = ''.join(msg).replace('\n', '')
print(txt)

root = Tk()
root.geometry('60x8')
root.title('課堂練習12-4')

L1 = Label(root, text='同學旅遊調查', bg='lightblue', width=20, font='細明體 20 bold')
L1.pack()

T1 = Text(root, font=("細明體", 14), wrap=WORD, width=50, height=5)
T1.insert(INSERT, txt)
T1.pack(side=LEFT)

Sx1 = Scrollbar(root, orient=HORIZONTAL)
Sy1 = Scrollbar(root)

Sx1.pack(side=BOTTOM, fill=X)
Sy1.pack(side=RIGHT, fill=Y)

Sx1.config(command=T1.xview)
Sy1.config(command=T1.yview)

T1.config(xscrollcommand=Sx1.set, yscrollcommand=Sy1.set)

root.mainloop()