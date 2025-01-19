names = ['巴哈', '貝多芬', '布拉姆斯', '柴可夫斯基', '孟德爾頌', '莫札特', '蕭邦', '比才']

name = input('請輸入姓名:')
if name not in names:
    print('%s在名單中是 False'%(name))
else:
    print('%s在名單中的第%d個位置'%(name, names.index(name)))