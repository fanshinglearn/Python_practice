import requests
url = r'https://tw.news.yahoo.com/%E9%AB%94%E5%9E%8B%E5%B7%AE%E5%A4%AA%E5%A4%9A%E5%93%A5%E5%90%89%E6%8B%89%E5%B0%8D%E9%87%91%E5%89%9B%E6%9C%83%E5%BD%A2%E6%88%90%E5%A4%A7%E8%A1%9B%E5%B0%8D%E6%8A%97%E6%AD%8C%E5%88%A9%E4%BA%9E-072717058.html'

# 下載網頁
try:
    r = requests.get(url)
    r.raise_for_status()
except:
    print('網頁下載錯誤')


find = input('請輸入搜尋字串：')

# 出現次數
fn = 'B10802050課堂練習15-2.txt'
print(f'{find} 在文章中出現的次數為 {r.text.count(find)} 次')

# 存檔
with open(fn, 'wb') as f:
    f.write(r.content)

# 長度
with open(fn, 'r', encoding='utf-8') as f:
    lines = f.readlines()

length = 0
c = 0
for line in lines:
    length += len(line)
    c += line.count(find)    

print(f'讀取結果的長度為 {length}')
print(f'{find} 在 {fn} 中出現的次數為 {c} 次')
