import requests
from bs4 import BeautifulSoup

url = r'https://cs.chu.edu.tw/'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

author_tag = soup.select('#author')
p_tag = soup.select('p')
td_tag = soup.select('td')
img_tag = soup.select('img')

print(f'author\t : {len(author_tag)}')
print(f'p\t : {len(p_tag)}')
print(f'td\t : {len(td_tag)}')
print(f'img\t : {len(img_tag)}')

for p in p_tag:
    print(p.text)

for img in img_tag:
    print(img['src'])
