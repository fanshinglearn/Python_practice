import bs4, requests, os

date = input('請輸入欲查詢其別： ')
if date == '11201':
    url = 'https://invoice.etax.nat.gov.tw/index.html'
elif date == '11111':
    url = 'https://invoice.etax.nat.gov.tw/lastNumber.html'

html = requests.get(url)
print('網頁下載中 ...')
html.raise_for_status()
print('網頁下載完成')
print()

soup = bs4.BeautifulSoup(html.text, 'lxml')
award = soup.select('p.etw-tbiggest')

print(f'特別獎\t： {award[0].text}')
print(f'特獎\t： {award[1].text}')
print(f'頭獎1\t： {award[2].text.strip()}')
print(f'頭獎2\t： {award[3].text.strip()}')
print(f'頭獎3\t： {award[4].text.strip()}')
