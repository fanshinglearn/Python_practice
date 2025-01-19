import tkinter as tk
import random

root = tk.Tk()
root.geometry("350x200+200+300")
root.title('我的視窗')

choice = tk.StringVar()
choice.set(random.choice(['大', '小']))

def update_label():
    if choice.get() == '大':
        choice.set('小')
    else:
        choice.set('大')

L1 = tk.Label(root, text='請猜大小', textvariable=choice)
L1.pack()

B1 = tk.Button(root, text='猜我大', bg='#add8e6', fg='red', width=15, command=update_label)
B2 = tk.Button(root, text='猜我大', bg='#ffffe0', fg='red', width=15, command=update_label)
B3 = tk.Button(root, text='Exit', command=root.destroy)
B1.pack(side='left')
B2.pack(side='right')
B3.pack(side='bottom')

root.mainloop()
