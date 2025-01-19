import tkinter as tk
from tkinter import messagebox

def menu1_action():
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, "逢甲夜市，饒河夜市，瑞豐夜市")
    text_box.pack()

def menu2_action():
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, "基隆夜市，大東夜市，士林夜市")
    text_box.pack()

def menu3_action():
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, "花園夜市，中原夜市，羅東夜市")
    text_box.pack()

def show_about():
    messagebox.showinfo("功能說明", "介紹好吃小吃相關夜市")

def exit_program():
    root.destroy()

# 創建主視窗
root = tk.Tk()
root.title("夜市")

# 創建選單欄
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# 創建第一個選單
menu1 = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="好吃", menu=menu1)
menu1.add_command(label="雞排", command=menu1_action)
menu1.add_command(label="珍奶", command=menu2_action)
menu1.add_command(label="滷味", command=menu3_action)

# 創建第二個選單
menu2 = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="程式", menu=menu2)
menu2.add_command(label="功能說明", command=show_about)
menu2.add_separator()
menu2.add_command(label="結束", command=exit_program)

# 創建文字框
text_box = tk.Text(root, height=3, width=30)
text_box.pack()

# 隱藏文字框
text_box.pack_forget()

# 執行主迴圈
root.mainloop()
