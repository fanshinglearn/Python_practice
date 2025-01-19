import bs4, requests, os

url = 'https://www.sanrio.com.tw/'

html = requests.get(url)
print('網頁下載中 ...')
html.raise_for_status()
print('網頁下載完成')

soup = bs4.BeautifulSoup(html.text, 'lxml')
img_tag = soup.select('img')

print(f'搜尋到的圖片數量 = {len(img_tag)}')

i = 1
if len(img_tag) > 0:
    dir = 'B10802050課堂練習15-5'
    if os.path.exists(dir) == False:
        os.mkdir(dir)
    for img in img_tag:
        img_url = img['src']

        picture = requests.get(img_url)
        picture.raise_for_status()

        with open(f'{dir}/{os.path.basename(img_url)}', 'wb') as file:
            file.write(picture.content)
        print(f'{img_url} 圖片下載成功')
