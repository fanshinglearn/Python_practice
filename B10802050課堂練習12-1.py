import tkinter

root = tkinter.Tk()

# 視窗大小
w = 600
h = 480

# 視窗位置
x = int((root.winfo_screenwidth() - w) / 3)
y = int((root.winfo_screenheight() - h) / 4)
root.geometry(f'{w}x{h}+{x}+{y}')

# 視窗標題
root.title('何祐任的視窗')

# 視窗圖示
root.iconbitmap('chicken.ico')

# 視窗背景顏色
root.configure(bg='Purple')

root.mainloop()
