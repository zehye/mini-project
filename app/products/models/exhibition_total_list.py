from django.db import models


class ExhibitionTotalList(models.Model):
    """
    전시, 공연 정보들이 전체 다 하나의 페이지에 보여지는 리스트
    """
    thumbnail = models.ImageField(upload_to='exhibition_list', blank=True)
    title = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
