import re
import requests
from bs4 import BeautifulSoup

url = r'https://movies.yahoo.com.tw/movieinfo_main/MIB%E6%98%9F%E9%9A%9B%E6%88%B0%E8%AD%A6-%E8%B7%A8%E5%9C%8B%E8%A1%8C%E5%8B%95-men-in-black-international-9308?guccounter=1'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

pattern = r'(\w{0,4})?遜'

# 搜尋整個網頁
# text = soup.text

# names = re.findall(pattern, text)

# print('最後一個字為遜的名字：')
# [print(f'{name}遜') for name in names]

# 只搜尋演員
actors = [actor.text.strip() for actor in soup.select('span.movie_intro_list a')]

print('所有演員：')
[print(actor) for actor in actors]

names = [re.search(pattern, actor).group() for actor in actors if re.search(pattern, actor)]

print('\n最後一個字為遜的名字：')
[print(name) for name in names]
