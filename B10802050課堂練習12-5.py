import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def show_selected_items():
    selected_table = table.get()
    selected_appetizer = [appetizer_labels[i] for i in range(len(appetizer_choices)) if appetizer_choices[i].get()]
    selected_soup = [soup_labels[i] for i in range(len(soup_choices)) if soup_choices[i].get()]
    selected_main = [main_labels[i] for i in range(len(main_choices)) if main_choices[i].get()]
    selected_dessert = [dessert_labels[i] for i in range(len(dessert_choices)) if dessert_choices[i].get()]

    order_time = datetime.now().strftime("%Y年%m月%d日%H時%M分%S秒")

    order_summary = f"第{selected_table}桌點的菜單為\n開胃菜：{', '.join(selected_appetizer)}\n湯品：{', '.join(selected_soup)}\n主菜：{', '.join(selected_main)}\n甜點：{', '.join(selected_dessert)}"
    messagebox.showinfo("點菜確認", order_summary + "\n時間：" + order_time)

root = tk.Tk()
root.title("冰其林三星")

# 桌號選擇
table = tk.IntVar()
table.set(1)  # 預設選擇第一桌
table_frame = tk.Frame(root)
table_frame.pack()
for i in range(1, 7):
    table_button = tk.Radiobutton(table_frame, text=f"桌號 {i}", variable=table, value=i)
    table_button.pack(side=tk.LEFT)

# 開胃菜選擇
appetizer_frame = tk.Frame(root)
appetizer_frame.pack()
appetizer_label = tk.Label(appetizer_frame, text="開胃菜：")
appetizer_label.pack(side=tk.LEFT)
appetizer_choices = []
appetizer_labels = ["凱薩莎拉", "鮮蝦蘆筍", "水果沙拉"]
selected_appetizers = []
for i in range(len(appetizer_labels)):
    appetizer_var = tk.BooleanVar()
    appetizer_choices.append(appetizer_var)
    appetizer_checkbox = tk.Checkbutton(appetizer_frame, text=appetizer_labels[i], variable=appetizer_var)
    appetizer_checkbox.pack(side=tk.LEFT)

# 湯品選擇
soup_frame = tk.Frame(root)
soup_frame.pack()
soup_label = tk.Label(soup_frame, text="湯品：")
soup_label.pack(side=tk.LEFT)
soup_choices = []
soup_labels = ["阿里山香菇土雞湯", "永安清燉石斑魚湯", "七股溼地蛤蠣濃湯", "台南溫體牛肉清湯"]
selected_soups = []
for i in range(len(soup_labels)):
    soup_var = tk.BooleanVar()
    soup_choices.append(soup_var)
    soup_checkbox = tk.Checkbutton(soup_frame, text=soup_labels[i], variable=soup_var)
    soup_checkbox.pack(side=tk.LEFT)

# 主菜選擇
main_frame = tk.Frame(root)
main_frame.pack()
main_label = tk.Label(main_frame, text="主菜：")
main_label.pack(side=tk.LEFT)
main_choices = []
main_labels = ["超級厚黑牛排", "夭壽鮮嫩魚排", "不好吃砍頭雞排", "36D鴨胸"]
selected_mains = []
for i in range(len(main_labels)):
    main_var = tk.BooleanVar()
    main_choices.append(main_var)
    main_checkbox = tk.Checkbutton(main_frame, text=main_labels[i], variable=main_var)
    main_checkbox.pack(side=tk.LEFT)

# 甜點選擇
dessert_frame = tk.Frame(root)
dessert_frame.pack()
dessert_label = tk.Label(dessert_frame, text="甜點：")
dessert_label.pack(side=tk.LEFT)
dessert_choices = []
dessert_labels = ["法式布蕾", "炭烤布丁", "巧克力冰淇淋磚", "橙汁奶酪"]
selected_desserts = []
for i in range(len(dessert_labels)):
    dessert_var = tk.BooleanVar()
    dessert_choices.append(dessert_var)
    dessert_checkbox = tk.Checkbutton(dessert_frame, text=dessert_labels[i], variable=dessert_var)
    dessert_checkbox.pack(side=tk.LEFT)

# 確認鍵
confirm_frame = tk.Frame(root)
confirm_frame.pack()
confirm_button = tk.Button(confirm_frame, text="顯示已選擇的菜色", command=show_selected_items)
confirm_button.pack()

root.mainloop()
