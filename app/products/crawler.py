import requests
from bs4 import BeautifulSoup

response = requests.get('https://swindow.naver.com/art/external/booking/more')
soup = BeautifulSoup(response.text, 'lxml')

product_list = soup.select('li.list')
for product in product_list:
    thumbnail = product.select_one('img.img').get('src')
    title = product.select_one('strong.tit').get_text(strip=True)
    place = product.select_one('em.place').get_text(strip=True)
    duration = product.select_one('span.duration').get_text(strip=True)

    print(thumbnail)
    print(title)
    print(place)
    print(duration)