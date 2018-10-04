import requests
from bs4 import BeautifulSoup


class GetExhibitionTotalList:
    def get_exhibition_total_list(self):
        response = requests.get('https://swindow.naver.com/art/external/booking/more')
        soup = BeautifulSoup(response.text, 'lxml')
        product_list = soup.select('li.list')

        exhibition_total_list = list()

        for product in product_list:
            thumbnail = product.select_one('img.img').get('src')
            title = product.select_one('strong.tit').get_text(strip=True)
            place = product.select_one('em.place').get_text(strip=True)
            duration = product.select_one('span.duration').get_text(strip=True)

            exhibition_total_dict = dict()
            exhibition_total_dict['thumbnail'] = thumbnail
            exhibition_total_dict['title'] = title
            exhibition_total_dict['place'] = place
            exhibition_total_dict['duration'] = duration

            exhibition_total_list.append(exhibition_total_dict)
        return exhibition_total_list



if __name__ == '__main__':
    GetExhibitionTotalList().get_exhibition_total_list()
