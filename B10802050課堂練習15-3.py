import requests
from bs4 import BeautifulSoup

url = r'https://tw.news.yahoo.com/%E9%AB%94%E5%9E%8B%E5%B7%AE%E5%A4%AA%E5%A4%9A%E5%93%A5%E5%90%89%E6%8B%89%E5%B0%8D%E9%87%91%E5%89%9B%E6%9C%83%E5%BD%A2%E6%88%90%E5%A4%A7%E8%A1%9B%E5%B0%8D%E6%8A%97%E6%AD%8C%E5%88%A9%E4%BA%9E-072717058.html'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

# print(soup.text)
tag_list = soup.find_all('p')
# print(tag_list)
for tag in tag_list:
    print(tag.text)
# text_list = [soup.text]
# print(text_list)

# find_str = input('請輸入搜尋字串: ')
# count = 0
# for text in text_list:
#     if find_str in text:
#         x = text.count(find_str)
#         count += x

# print(f'{find_str} 在文章中出現的次數為 {count} 次')

# fn = 'B10802050課堂練習15-3.txt'
# with open(fn, 'w', encoding='utf-8') as f:
#     f.writelines(text_list)