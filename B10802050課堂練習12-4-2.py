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


# 性別選項鈕
gender_label = Label(root, text="性別：", font=("細明體", 14))
gender_label.pack(anchor=W)
gender_var = StringVar()
gender_var.set('男性')
male_radio = Radiobutton(root, text="男性", font=("細明體", 14), variable=gender_var, value="男性")
male_radio.pack(anchor=W)
female_radio = Radiobutton(root, text="女性", font=("細明體", 14), variable=gender_var, value="女性")
female_radio.pack(anchor=W)

# 星座選項鈕
zodiac_label = Label(root, text="星座：", font=("細明體", 14))
zodiac_label.pack(anchor=W)
zodiac_var = StringVar()
zodiac_var.set('牧羊座')
zodiac_list = ["牧羊座", "金牛座", "雙子座", "巨蟹座", "獅子座", "處女座", "天秤座", "天蠍座", "射手座", "摩羯座", "水瓶座", "雙魚座"]
for zodiac in zodiac_list:
    zodiac_radio = Radiobutton(root, text=zodiac, font=("細明體", 14), variable=zodiac_var, value=zodiac)
    zodiac_radio.pack(anchor=W)

# 最愛地點選項鈕
location_label = Label(root, text="最愛地點：", font=("細明體", 14))
location_label.pack(anchor=W)
location_var = StringVar()
location_var.set('龜山島')
location_list = ["龜山島", "澎湖群島", "金門馬祖", "小琉球", "綠島", "蘭嶼"]
for location in location_list:
    location_radio = Radiobutton(root, text=location, font=("細明體", 14), variable=location_var, value=location)
    location_radio.pack(anchor=W)

root.mainloop()