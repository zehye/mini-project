from django.db import models

from .. import crawler

__all__ = (
    'ExhibitionTotalList',
)


class ExhibitionTotalList(models.Model):
    """
    전시, 공연 정보들이 전체 다 하나의 페이지에 보여지는 리스트
    """
    thumbnail = models.ImageField(upload_to='exhibition_list', blank=True)
    title = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

    def get_exhibition_total_list_crawler(self):
        """
        products.crawler함수를 호출하는 함수
        :return: 전시의 전체 리스트를 크롤링해온 정보
        """
        exhibition_total_list = crawler.GetExhibitionTotalList().get_exhibition_total_list()
        return exhibition_total_list

    def create_exhibition_total_list(self):
        """
        위 함수를 실행시켜 얻은 exhibition_total_list를 통해 각 전시들의 인스턴스를 생성
        :return: 각 전시들에 맞는 인스턴스
        """
        exhibition_list = self.get_exhibition_total_list_crawler()
        for exhibition in exhibition_list:
            ExhibitionTotalList.objects.create(
                thumbnail=exhibition['thumbnail'],
                title=exhibition['title'],
                place=exhibition['place'],
                duration=exhibition['duration'],
            )


if __name__ == '__main__':
    ExhibitionTotalList()
